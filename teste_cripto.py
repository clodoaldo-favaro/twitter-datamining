from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes




def criptografar(data_file):
    key = get_random_bytes(32)
    with open('chave.bin', 'wb') as f:
        f.write(key)
    cipher = AES.new(key, AES.MODE_EAX)

    with open(data_file, 'r') as f:
        data = f.read().encode('utf-8')

    ciphertext, tag = cipher.encrypt_and_digest(data)

    with open(data_file + '.enc', "wb") as f:
        [ f.write(x) for x in (cipher.nonce, tag, ciphertext) ]


def decrypt(encrypted_file):
    with open(encrypted_file, "rb") as f:
        nonce, tag, ciphertext = [f.read(x) for x in (16, 16, -1)]

    with open('chave.bin', 'rb') as f:
        key = f.read()

    cipher = AES.new(key, AES.MODE_EAX, nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)

    with open(encrypted_file[:-4], 'wb') as f:
        f.write(data)

