class Stack:
    list = []
    size = 0
    def pop(self):
        self.size -= 1
        return self.list.pop(-1)

    def push(self, value):
        self.list.append(value)
        self.size += 1

    def getNext(self):
        return self.list[-1]

    def getSize(self):
        return self.size

    def inventory(self):
        return self.list
