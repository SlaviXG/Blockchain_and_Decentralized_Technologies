from Transaction import *

'''
Block class

'''


class Block:

    def __init__(self, setOfTransactions, prevHash):

        self.setOfTransactions = setOfTransactions
        self.prevHash = prevHash

        tsx_str = ""
        for tx in self.setOfTransactions:
            tsx_str += str(tx)
        self.blockID = hashlib.sha256((tsx_str + str(prevHash)).encode('utf-8')).hexdigest()

    def __str__(self):
        tsx_str = ""
        for tx in self.setOfTransactions:
            tsx_str += str(tx)
        return "Block_ID: " + str(self.blockID) + "\nPrev_Hash: " + str(self.prevHash) + '\n' + "Transactions:\n" + tsx_str + '\n'


'''
Blockchain class

'''


class Blockchain:

    def __init__(self):
        # creating the first tx
        first_tx = Transaction([], 0)
        # creating genesis block
        genesis = Block([first_tx], 0)
        self.blockHistory = [genesis]
        self.txDatabase = [first_tx]

    def validateBlock(self, block: Block):
        pass
