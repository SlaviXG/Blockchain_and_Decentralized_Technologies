from Account_and_Operation import *

'''
Transaction class
- stores operations
- has nonce
'''


class Transaction:
    def __init__(self, setOfOperations, nonce):
        self.nonce = nonce
        self.setOfOperations = setOfOperations
        ops_str = ""
        for op in setOfOperations:
            self.ops_str += op
        self.ID = hashlib.sha256((ops_str + str(nonce)).encode('utf-8')).hexdigest()

    def __str__(self):
        ops_str = ""
        for op in setOfOperations:
            self.ops_str += op
        return "Nonce : " + str(self.nonce) + ops_str
