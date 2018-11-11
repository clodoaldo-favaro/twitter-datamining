from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from os.path import isfile
from os import remove


def encrypt(data_file, count=''):
    # Gera uma chave aleaatória inicial de 256 bits (32 bytes)
    key = get_random_bytes(32)

    with open('chave' + count + '.bin', 'wb') as f:
        f.write(key)


    # Cria a chave secreta (256 bits)
    cipher = AES.new(key, AES.MODE_EAX)

    # Le o arquivo a ser criptografado
    try:
        with open(data_file, 'r') as f:
            data = f.read().encode('utf-8')
    except FileNotFoundError as e:
        print('Arquivo nao encontrado {0}'.format(e))
        return

    # Criptografa os dados lidos
    ciphertext, tag = cipher.encrypt_and_digest(data)

    # Escreve os dados criptografados em um arquivo
    with open(data_file + '.enc', "wb") as f:
        [ f.write(x) for x in (cipher.nonce, tag, ciphertext) ]


#*******************************************************************************************************
#*******************************************************************************************************
#*******************************************************************************************************


def decrypt(encrypted_file, output_code='', key_file=''):

    try:
        with open(encrypted_file, "rb") as f:
            nonce, tag, ciphertext = [f.read(x) for x in (16, 16, -1)]
    except FileNotFoundError as e:
        print('Arquivo nao encontrado {0}'.format(e))
        return

    # Lê a chave do arquivo
    try:
        # Se o nome do arquivo chave nao for passado, assume chave.bin como arquivo chave
        if key_file == '':
            with open('chave.bin', 'rb') as f:
                key = f.read()
        else:
            with open(key_file, 'rb') as f:
                key = f.read()


    except FileNotFoundError as e:
        print('Arquivo nao encontrado {0}'.format(e))
        return

    cipher = AES.new(key, AES.MODE_EAX, nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)

    with open(output_code + encrypted_file[:-4], 'wb') as f:
        f.write(data)

