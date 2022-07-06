from Signature import *
from Account import Account
import hashlib


'''
Operation Class

Constructor :
    initiates a data exchange
    
boolean verifyOperation :
    returns if the operation is valid
 
'''


class Operation:
    def __init__(self, sender: Account, receiver, field: str, value: str, signature: Signature):
        self.sender = sender        # Account
        self.receiver = receiver    # Account
        self.item = (field, value)  # Item (key_in_dictionary, value)
        self.signature = signature  # Signature

    def verifyOperation(self):
        if self.item[0] == '' or self.item[1] == '':
            return false
        return true

    def __str__(self):
        return str(sender.ID) + "\n -> \n" + str(receiver.ID) + "\n" + field + " : " + value

    def print(self):
        print(str(self)) + "\n"
