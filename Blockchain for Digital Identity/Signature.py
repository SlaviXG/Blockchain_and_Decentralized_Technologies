from KeyPair import *

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


class Signature:

    def __init__(self):
        self.signature = None

    def signData(self, private_key, message):
        self.signature = private_key.sign(
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return self.signature

    def verifySignature(self, realSig, message, public_key):
        try:
            public_key.verify(
                realSig,
                message,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
        except:
            return False

        return True

    def printSignature(self):
        print(self.signature)
