import Accont


class Operation:
    def __init__(self, sender, receiver, data, signature):
        self.sender = sender
        self.receiver = receiver
        self.data = data
        self.signature = signature

    def verifyOperation(self):
        pass