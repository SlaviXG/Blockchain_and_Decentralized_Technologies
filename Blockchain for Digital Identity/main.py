
from Transaction import *


#x = KeyPair()
#x.printKeyPair()

#sig = Signature()
#enc = sig.signData(x.privateKey, "abacaba")

#print(sig.verifySignature(enc, "abacabb", x.publicKey))
#print(sig.verifySignature(enc, "abacaba", x.publicKey))

#sig.printSignature()

first = Identity("Tim")
second = Identity("Jake")
#print(firstOne.toString())
#print(firstOne.name)
#print(first.ID)

first.personal_data["123"] = 0
op = first.createOperation(second, "123")
#print(second.received_data)

print(op.verifyOperation())