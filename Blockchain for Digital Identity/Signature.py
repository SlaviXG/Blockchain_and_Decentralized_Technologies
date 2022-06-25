from KeyPair import KeyPair

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


class Signature:

    def signData(self, private_key, message):
        pass

    def verifySignature(self, realSig, message, public_key):
        pass

    def printSignature(self):
        pass