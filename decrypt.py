from encrypt_decrypt import *

msg = [363395, 53736, 146399, 146399, 241763, 83449] #List of encrypted letters
private_key = (29051, 404471)


def decrypt(pk, ciphertext):
    print("Decrypting...")
    key, n = pk
    plain = [chr((char ** key) % n) for char in ciphertext]
    return ''.join(plain)


print(decrypt(private_key, msg))
