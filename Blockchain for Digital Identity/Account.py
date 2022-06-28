from KeyPair import KeyPair
from Signature import Signature


class Account:

    # Constructor
    def __init__(self, name):
        # Identifier = SHA-1 hash
        self.ID = None
        # Key Pair (wallet)
        self.key_pair = KeyPair()
        # Name
        self.name = name

    # returns the string with the account object
    def toString(self):
        pass

    # Prints the Key Pair
    def printKeyPair(self):
        self.key_pair.printKeyPair()


class Identity(Account):
    pass

class Organization(Account):
    pass
