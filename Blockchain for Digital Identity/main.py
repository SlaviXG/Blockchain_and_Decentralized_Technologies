﻿from Signature import *

from Account import *

#x = KeyPair()
#x.printKeyPair()

#sig = Signature()
#enc = sig.signData(x.privateKey, b"abacaba")

#print(sig.verifySignature(enc, b"abacabb", x.publicKey))
#print(sig.verifySignature(enc, b"abacaba", x.publicKey))

#sig.printSignature()

firstOne = Account("Tim")
print(firstOne.toString())