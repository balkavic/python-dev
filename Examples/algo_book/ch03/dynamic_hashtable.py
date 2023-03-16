from entry import Entry
from entry import LinkedEntry


class DynamicHashTable:
    def __init__(self, M=10):
        self.table = [None] * M
        self.M = M
        self.N = 0

        self.load_factor = 0.75
        self.threshold = min(M * self.load_factor, M - 1)

    def get(self, k):
        hc = hash(k) % self.M
        entry = self.table[hc]
        while entry:
            if entry.key == k:
                return entry.value
            entry = entry.next
        return None

    def get_hash(self, k):
        for i in range(len(self.table)):
            if self.table[i]:
                if self.table[i].key == k:
                    return i
        return None

    def put(self, k, v):
        hc = hash(k) % self.M
        entry = self.table[hc]
        while entry:
            if entry.key == k:
                entry.value = v
                return
            entry = entry.next

        self.table[hc] = LinkedEntry(k, v, self.table[hc])
        self.N += 1

        if self.N >= self.threshold:
            self.resize(2 * self.M + 1)

    def remove(self, k):
        hc = hash(k) % self.M
        entry = self.table[hc]
        prev = None
        while entry:
            if entry.key == k:
                if prev:
                    prev.next = entry.next
                else:
                    self.table[hc] = entry.next

                self.N -= 1
                return entry.value

            prev, entry = entry, entry.next

        return None

    def resize(self, new_size):
        temp = DynamicHashTable(new_size)
        for n in self.table:
            while n:
                temp.put(n.key, n.value)
                n = n.next
            self.table = temp.table
            self.M = temp.M
            self.threshold = self.load_factor * self.M



