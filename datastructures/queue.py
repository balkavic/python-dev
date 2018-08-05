class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None

    def isEmpty(self):
        return self.first is None

    def get_first(self):
        if self.first:
            return self.first.data
        else:
            return None

    def queue(self, data):
        node = Node(data)
        if self.first is None:
            self.first = node
        else:
            self.last.next = node
        self.last = node

    def dequeue(self):
        if self.first is None:
            return None
        else:
            data = self.first.data
            self.first = self.first.next
        return data


