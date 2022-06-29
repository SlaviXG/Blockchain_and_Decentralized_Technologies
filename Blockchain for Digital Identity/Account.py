from KeyPair import KeyPair
from Signature import Signature

import hashlib


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
        self.ID = hashlib.sha256(str(self).encode('utf-8')).hexdigest()

    def createOperation(self):
        pass

    def signData(self, message):
        sign = Signature()
        return sign.signData(self.key_pair.privateKey, message)

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
