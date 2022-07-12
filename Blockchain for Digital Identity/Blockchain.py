from Transaction import *

'''
Block class
- contains transactions
- contains hash of prev block

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
- contains blocks
- blocks can be validated and added to the history
'''


class Blockchain:

    def __init__(self):
        # creating the first tx
        first_tx = Transaction([], 0)
        # creating genesis block
        self.genesisBlock = Block([first_tx], 0)
        self.blockHistory = [self.genesisBlock]
        self.txDatabase = [first_tx]

    def validateBlock(self, block: Block):
        # checking hash of previous block
        if block.prevHash != self.blockHistory[-1].blockID:
            return
        # going through transactions in block
        for tx in block.setOfTransactions:
            # checking if the tx is already in history
            if tx in self.txDatabase:
                return
            # going through exchange operations in the transaction
            for op in tx.setOfOperations:
                # operation verification
                if not op.verifyOperation:
                    return

        # validation process
        self.blockHistory.append(block)
        for tx in block.setOfTransactions:
            self.txDatabase.append(tx)

    def printBlockHistory(self):
        print("---------------------------------------------------------------------------")
        print("Block History.\n")
        for block in self.blockHistory:
            print(block)
        print("---------------------------------------------------------------------------")