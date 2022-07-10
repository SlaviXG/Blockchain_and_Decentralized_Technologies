from Transaction import *

'''
Block class

'''

class Block:
    def __init__(self, setOfTransactions, prevHash):

        self.setOfTransactions = setOfTransactions
        self.prevHash = prevHash

        tsx_str = ""
        for tx in setOfTransactions:
            self.tsx_str += tx
        self.blockID = hashlib.sha256((tsx_str + str(prevHash)).encode('utf-8')).hexdigest()

    def __str__(self):
        tsx_str = ""
        for tx in setOfTransactions:
            self.tsx_str += tx
        return "Block_ID: " + str(self.blockID) + "\nPrev_Hash: " + self.prevHash + '\n' + tsx_str + '\n'


'''
Blockchain class

'''


class Blockchain:
    pass
