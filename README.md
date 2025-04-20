🛠️ JW_Key
JW_Key est un outil Python simple permettant de :

Décoder un JWT et extraire sa clé JWK intégrée.

Reconstruire la clé RSA publique ou privée à partir du JWK.

Afficher les informations de clé intégrées ou les IDs de clé (kid).

📖 Décodage du header JWT en Base64.

🔍 Extraction de clé JWK embarquée dans le JWT.

🛠️ Reconstruction et export en PEM de la clé publique ou privée.

📑 Gestion des JWT avec champ kid uniquement.

🛑 Gestion des erreurs simple.

📚 Prérequis
Python 3

Modules Python :

bash
Copy
Edit
pip install jwcrypto pyfiglet colorama
🚀 Utilisation
Lance le script

bash
Copy
Edit
python3 jw_key.py
Colle ton JWT quand demandé

text
Copy
Edit
[*] Enter JWT here : eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImp3ayI6...
Le script :

Affiche le JWT reçu

Décode et extrait le JWK si présent

Reconstruit et affiche la clé RSA en PEM (publique ou privée)

📌 Exemple de résultat
text
Copy
Edit
[!] Here your JWT ->
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImp3ayI6...

[*] Now the JWT with good parsing

[!] Embedded Key -> {"kty":"RSA","n":"...","e":"AQAB"}

[*] Now reconstructing the RSA key....
[!] There is a public key !!! ->
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkq...
-----END PUBLIC KEY-----
📖 Explication rapide
decode_jwt() : décode l'entête JWT et récupère la clé JWK ou l'ID de clé.

reconstruct_rsa() : reconstruit la clé RSA à partir du JWK (PEM).

📂 Arborescence
Copy
Edit
JW_Key/
 ├── jw_key.py
 ├── README.md
🛡️ Disclaimer
⚠️ Ce script est à usage pédagogique et de test uniquement.
Il ne doit pas être utilisé en production ni à des fins illégales.

📬 Auteur
[@T3Nat]
