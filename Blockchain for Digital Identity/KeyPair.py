from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

class keyPair:

    def __init__(self):
        self.genKeyPair()
        self.pubKStr = self.publicKey.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        self.priKStr = self.privateKey.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )

    def genKeyPair(self):
        self.privateKey = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        self.publicKey = self.privateKey.public_key()

    def printKey(self):
        print(self.priKStr)
        print(self.pubKStr, '\n')
        with open('keys/private_key.pem', 'wb') as f:
            f.write(self.priKStr)
        with open('keys/public_key.pem', 'wb') as f:
            f.write(self.pubKStr)


# Used these examples :
# https://nitratine.net/blog/post/asymmetric-encryption-and-decryption-in-python/
#