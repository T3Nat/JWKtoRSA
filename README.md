# JW_Key

**JWT Key Extraction & RSA Reconstruction Tool**

Outil offensif d'extraction et de reconstruction de clés cryptographiques embarquées dans des JSON Web Tokens. Conçu pour les pentesters et les joueurs de CTF.

---

## Cas d'usage en pentest

| Scénario | Ce que fait JW_Key |
|---|---|
| JWT avec JWK embarqué dans le header | Extrait la clé et reconstruit le PEM |
| Clé publique RSA récupérable | Permet ensuite une attaque **HMAC confusion** (RS256 → HS256) |
| Clé privée exposée par erreur | Extraction directe → signature de tokens arbitraires |
| Champ `kid` présent | Détection pour investigation (path traversal, SQLi) |

> Une clé publique extraite d'un JWT peut suffire à forger des tokens valides si le serveur accepte l'algorithme HS256 avec cette même clé.

---

## Installation

```bash
git clone https://github.com/T3Nat/JW_Key.git
cd JW_Key
pip install jwcrypto pyfiglet colorama
```

**Prérequis :** Python 3.8+

---

## Utilisation

```bash
python3 jw_key.py
```

```
[*] Enter JWT here : eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImp3ayI6ey...

[!] Here your JWT ->
 eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImp3ayI6ey...

[*] Now the JWT with good parsing

[!] Embedded Key -> {"kty":"RSA","n":"...","e":"AQAB"}
[*] Now reconstructing the RSA key....
[!] There is a public key !!! ->
 -----BEGIN PUBLIC KEY-----
 MIIBIjANBgkq...
 -----END PUBLIC KEY-----
```

---

## Workflow type en pentest

```
1. Intercepter un JWT (Burp, DevTools, proxy)
2. JW_Key → extraire la clé publique PEM
3. Utiliser la clé pour :
   - Forger un token HS256 signé avec la clé publique (HMAC confusion)
   - Identifier le type de clé et chercher des faiblesses (taille RSA faible, etc.)
   - Injecter son propre JWK dans le header si le serveur le valide
```

---

## Structure

```
JW_Key/
├── jw_key.py      # Script principal
└── README.md
```

---

## Limitations actuelles

- Supporte uniquement l'extraction JWK depuis le header JWT
- Pas de forge de token intégrée (utiliser `pyjwt` ou `jwt_tool` en complément)
- Pas de bruteforce de secret HMAC
- Gestion d'erreurs basique

---

## Outils complémentaires

| Outil | Usage |
|---|---|
| [jwt_tool](https://github.com/ticarpi/jwt_tool) | Suite complète d'attaques JWT |
| [jwt.io](https://jwt.io) | Décodage rapide en ligne |
| Burp Suite + JWT Editor | Manipulation de tokens en live |

---

## Disclaimer

⚠️ **Usage autorisé uniquement dans un cadre légal** : pentests avec autorisation écrite, CTF, labs personnels. L'auteur décline toute responsabilité en cas d'utilisation malveillante.

---

## Auteur

[@T3Nat](https://github.com/T3Nat)
