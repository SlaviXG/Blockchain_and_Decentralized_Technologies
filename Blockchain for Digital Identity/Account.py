from KeyPair import KeyPair
from Signature import Signature


class Account:

    # Constructor
    def __init__(self, name: str):
        # Key Pair (wallet)
        self.key_pair = KeyPair()
        # Name
        self.name = name
        # Identifier = SHA-1 hash
        self.ID = None

    def createOperation(self):
        pass

    def signData(self):
        pass

    #def __str__(self):
    #    pass

    # returns the string with the account object
    def toString(self):
        return str(self)

    # Prints the Key Pair
    def printKeyPair(self):
        self.key_pair.printKeyPair()


class Identity(Account):

    def __init__(self, name):
        super(Identity, self).__init__(name)
        self.type = "Identity"


class Organization(Account):

    def __init__(self, name):
        super(Organization, self).__init__(name)
        self.type = "Organization"
