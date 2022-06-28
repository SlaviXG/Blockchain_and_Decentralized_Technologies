from KeyPair import KeyPair
from Signature import Signature


class Account:

    # Constructor
    def __init__(self):
        # Identifier = SHA-1 hash
        self.ID = None
        # Key Pair
        self.key_pair = None
        # Name
        self.name = None

    # Prints the account information
    def print(self):
        pass


class Identity(Account):
    pass

class Organization(Account):
    pass
