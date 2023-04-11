class Node:
    next = ''
    value = ''
    blnHead = False
    blnTail = False

    def __init__(self, value = '', next = '', blnHead = False, blnTail = False):
        self.next = next
        self.value = value
        self.blnHead = blnHead
        self.blnTail = blnTail
    def getValue(self):
        return self.value
    def setValue(self, value):
        self.value = value
    def getNext(self):
        return self.next
    def setNext(self, next):
        self.next = next
    def isHead(self):
        return self.blnHead
    def isTail(self):
        return self.blnTail

class SinglyLinkedList:
    Head = ''
    Tail = ''
    size = 0
    def __init__(self):
        self.Tail = Node(blnTail = True)
        self.Head = Node(blnHead = True, next = self.Tail)

    def insert(self, value, idx):
        New = Node(value = value)
        nodePrev = self.get(idx - 1)
        nodeNext = nodePrev.getNext()
        nodePrev.setNext(New)
        New.setNext(nodeNext)
        self.size += 1

    def remove(self, idx):
        nodePrev = self.get(idx - 1)
        nodeRemove = nodePrev.getNext()
        nodeNext = nodeRemove.getNext()
        nodePrev.setNext(nodeNext)
        self.size -= 1
        return nodeRemove.getValue()

    def get(self, idx):
        nodeReturn = self.Head
        for i in range(idx+1):
            nodeReturn = nodeReturn.getNext()
        return nodeReturn

    def Status(self):
        status = []
        nodeCurrent = self.Head
        while nodeCurrent.getNext().isTail() == False:
            nodeCurrent = nodeCurrent.getNext()
            status.append(nodeCurrent.getValue())
        return status

    def getSize(self):
        return self.size