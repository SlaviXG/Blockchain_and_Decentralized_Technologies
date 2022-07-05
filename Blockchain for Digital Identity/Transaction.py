import Operation


class Transaction:
    def __init__(self, nonce, setOfOperations):
        self.nonce = nonce
        self.setOfOperations = setOfOperations