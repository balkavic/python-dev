


class Entry:
    def __init__(self, k, v):
        self.key = k
        self.value = v

class HastTable:
    def __init__(self, M=10):
        self.table = [None] * M
        self.M = M

    def get(self, k):
        hc = hash(k) % self.M
        return self.table[hc].value if self.table[hc] else None

    def put(self, k, v):
        hc = hash(k) % self.M
        entry = self.table[hc]
        if entry:
            if entry.key == k:
                entry.value = v
            else:
                raise RuntimeError('Key Collision: {} and {}'.format(k, entry.key))
        else:
            self.table[hc] = Entry(k, v)


table = HastTable(1000)
table.put("April", 30)
table.put("May", 31)
table.put("September", 30)

print(table.get("August"))
print(table.get("September"))
