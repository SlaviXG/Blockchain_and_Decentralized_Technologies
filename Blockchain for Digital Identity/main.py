from Blockchain import Blockchain
from Blockchain import *


#x = KeyPair()
#x.printKeyPair()

#sig = Signature()
#enc = sig.signData(x.privateKey, "abacaba")

#print(sig.verifySignature(enc, "abacabb", x.publicKey))
#print(sig.verifySignature(enc, "abacaba", x.publicKey))

#sig.printSignature()

# first = Identity("Tim")
# second = Identity("Jake")
#print(firstOne.toString())
#print(firstOne.name)
#print(first.ID)

# first.personal_data["123"] = 0
# op = first.createOperation(second, "123")
# tx = Transaction([op])

#print(second.received_data)

#print(op.verifyOperation())

blockchain = Blockchain()
blockchain.printBlockHistory()


first = Identity("Tim")
second = Identity("Jake")
first.personal_data["123"] = 0
op = first.createOperation(second, "123")
tx = Transaction([op], 0)


block = Block([tx], 0)
blockchain.validateBlock(block)
#blockchain.printBlockHistory()

block = Block([tx], blockchain.blockHistory[0].blockID)
blockchain.validateBlock(block)
blockchain.printBlockHistory()