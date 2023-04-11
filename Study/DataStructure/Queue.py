class Queue:
    list = []
    size = 0
    def dequeue(self):
        self.size -= 1
        return self.list.pop(0)

    def enqueue(self, value):
        self.list.append(value)
        self.size += 1

    def getNext(self):
        return self.list[0]

    def getSize(self):
        return self.size

    def inventory(self):
        return self.list

class PriorityQueue:
    list = []
    size = 0

    def enqueue(self, value, priority):
        idx = 0
        for i in range(self.size):
            if self.list[idx][1] < priority:
                break
            idx += 1
        self.list.insert(idx, [value, priority])
        self.size += 1

    def dequeue(self):
        self.size -= 1
        return self.list.pop(0)

    def getNext(self):
        return self.list[0]

    def getSize(self):
        return self.size

    def inventory(self):
        return self.list
