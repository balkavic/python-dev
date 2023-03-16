from entry import Entry
from entry import LinkedEntry





class HashTable:
    def __init__(self, M=10):
        self.table = [None] * M
        self.M = M
        self.N = 0

    def get(self, k):
        hc = hash(k) % self.M
        while self.table[hc]:
            if self.table[hc].key == k:
                return self.table[hc].value
            hc = (hc + 1) % self.M
        return None

    def get_hash(self, k):
        for i in range(len(self.table)):
            if self.table[i]:
                if self.table[i].key == k:
                    return i
        return None

    def put(self, k, v):
        hc = hash(k) % self.M
        while self.table[hc]:
            if self.table[hc].key == k:
                self.table[hc].value = v
                return
            hc = (hc + 1) % self.M

        if self.N >= self.M - 1:
            raise RuntimeError('Table is full.')

        self.table[hc] = Entry(k, v)
        self.N += 1


