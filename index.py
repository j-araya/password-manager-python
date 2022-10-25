from masterkey import run_masterkey
from new_masterkey import run_new_masterkey

from utils import get_hash_bytes

if __name__ == '__main__':
    
    # Obtenemos el hash de la masterkey en bytes
    hash_bytes = get_hash_bytes()

    if hash_bytes is not None:
        # Ya se ha creado una masterkey
        run_masterkey(hash_bytes)
    else:
        # Primera vez que se utiliza el programa. Se debe crear una masterkey
        print('No Master Key. Create one...')
        run_new_masterkey()
        