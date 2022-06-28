from KeyPair import KeyPair
from Signature import Signature


class Account:

    # Constructor
    def __init__(self, name: str):
        # Identifier = SHA-1 hash
        self.ID = None
        # Key Pair (wallet)
        self.key_pair = KeyPair()
        # Name
        self.name = name

    def __str__(self):
        pass
    
    # returns the string with the account object
    def toString(self):
        return str(self)

    # Prints the Key Pair
    def printKeyPair(self):
        self.key_pair.printKeyPair()


class Identity(Account):
    pass

class Organization(Account):
    pass
