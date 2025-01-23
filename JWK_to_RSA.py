#!/usr/bin/env python3

import jwt
import base64
from jwcrypto import jwk
import json
from colorama import Fore,Style
import pyfiglet

banner = pyfiglet.figlet_format("JW_Key")
print(Fore.RED + banner)
print(Style.RESET_ALL)

def decode_jwt(token):
    
    # On décode le JWT qui est en Base64
    header_b64 = token.split('.')[0]
    header_json = base64.urlsafe_b64decode(header_b64 + '==').decode('utf-8')
    header = json.loads(header_json) # Conversoin de l'entête en objet JSON
    
    # On extract  
    if 'jwk' in header:
        jwk_data = header['jwk']
        return jwk.JWK.from_json(json.dumps(jwk_data))
    elif 'kid' in header:
        print(f"[!] Clé ID trouvée : {header['kid']}")
        return None
    else:
        print('[X] Valeurs incorrecte du JWK')

def reconstruct_rsa(token):
    # On stock le JWT/JWK en json dans une variable
    key = jwk.JWK.from_json(token)
    try:
        private = key.export_to_pem(private_key=True, password=None)
        if private:
            print(f'[!] There is a private key!!! -> \n {private.decode()}')
    except:
        public = key.export_to_pem(private_key=False, password=None)
        if public:
            print(f'[!] There is a public key !!! -> \n {public.decode()}')
         
    
# On injecte notre JWT dans le script en tant que variable
jwt = input('[*] Enter JWT here : ')
print('\n')
# Try Catch pour 
try:
    print(f'[!] Here your JWT -> \n {jwt}')    
except NameError as e:
    print(f'[X] Error with the JWT : {e}')
print('[*] Now the JWT with good parsing \n ')
try:
    jwk_key = decode_jwt(jwt)    
    if jwk_key:
        print(f'[!] Embedded Key -> {jwk_key.export()}')
        print('[*] Now reconstructing the RSA key....')
        jwk_key = jwk_key.export()
        jwk_key = reconstruct_rsa(jwk_key)
        print(jwk_key)
    else:
        print('[X] No key found!')
except NameError as i:
    print(f'[X] Error -> {i}')