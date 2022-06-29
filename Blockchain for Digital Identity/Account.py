from KeyPair import KeyPair
from Signature import Signature

from cryptography.hazmat.primitives import hashes


class Account:

    # Constructor
    def __init__(self, name: str, type: str):
        # Key Pair (wallet)
        self.key_pair = KeyPair()
        # Name
        self.name = name
        # Identity / Organization
        self.type = type
        # Identifier = SHA256 - hash
        hashes.Hash(hashes.SHA256()).update(str.encode(str(self), 'utf-8'))
        self.ID = hashes.Hash(hashes.SHA256()).finalize()

    def createOperation(self):
        pass

    def signData(self):
        pass

    def __str__(self):
        return self.name+self.type+str(self.key_pair.pubKStr)

    # returns the string with the account object
    def toString(self):
        return str(self)

    # Prints the Key Pair
    def printKeyPair(self):
        self.key_pair.printKeyPair()


class Identity(Account):

    def __init__(self, name):
        super(Identity, self).__init__(name, "Identity")


class Organization(Account):

    def __init__(self, name):
        super(Organization, self).__init__(name, "Organization")
