class Stack:

    def __init__(self, items=None, limit=100):
        if items is None:
            self.items = []
        else:
            self.items = list(items)
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if self.full():
            return
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

    def full(self):
        return self.size() >= self.limit

    def search(self, target):
        if target not in self.items:
            return -1
        
        return self.size() - 1 - self.items.index(target)
