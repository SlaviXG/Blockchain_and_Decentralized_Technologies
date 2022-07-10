#from Operation import *
from Account_and_Operation import *

'''

'''


class Transaction:
    def __init__(self, nonce, setOfOperations):
        self.nonce = nonce
        self.setOfOperations = setOfOperations
