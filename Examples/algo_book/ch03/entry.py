class Entry:
    def __init__(self, k, v):
        self.key = k
        self.value = v


class LinkedEntry:
    def __init__(self, k, v, rest=None):
        self.key = k
        self.value = v
        self.next = rest


