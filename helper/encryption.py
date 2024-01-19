from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import binascii
import os

IV_LENGTH = 16

def encrypt(text, key):
    iv = os.urandom(IV_LENGTH)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(pad(text.encode('utf-8'), AES.block_size))

    return {'iv': binascii.hexlify(iv).decode('utf-8'), 'encryptedData': binascii.hexlify(encrypted).decode('utf-8')}

def decrypt(data, key):
    iv = binascii.unhexlify(data['iv'])
    encrypted_text = binascii.unhexlify(data['encryptedData'])
    decipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = decipher.decrypt(encrypted_text)

    return unpad(decrypted, AES.block_size).decode('utf-8')
