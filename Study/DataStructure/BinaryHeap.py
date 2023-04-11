class BinaryHeap:

    arrPriority = {}
    arrValue = {}
    size = 0

    def __init__(self):
        self.arrPriority = {}
        self.arrValue = {}
        self.size = 0

    def enqueue(self, value, priority):
        self.arrPriority[self.size] = priority
        self.arrValue[self.size] = value
        self.size += 1
        self.percorlateUp(self.size-1)

    def percorlateUp(self, idx):
        if idx == 0:
            return
        parent = int( (idx-1)/2 )
        if self.arrPriority[parent] < self.arrPriority[idx]:
            self.arrPriority[parent], self.arrPriority[idx] = self.arrPriority[idx], self.arrPriority[parent]
            self.arrValue[parent], self.arrValue[idx] = self.arrValue[idx], self.arrValue[parent]
            self.percorlateUp(parent)

    def percorlateDown(self, idx):
        if 2*idx +1 >= self.size:
            return
        else:
            leftchild = 2*idx + 1
            leftPriority = self.arrPriority[leftchild]
        if 2*idx +2 >= self.size:
            rightPriority = -999999
        else:
            rightchild = 2*idx + 2
            rightPriority = self.arrPriority[rightchild]
        if leftPriority > rightPriority:
            biggerchild = leftchild
        else:
            biggerchild = rightchild
        if self.arrPriority[idx] < self.arrPriority[biggerchild]:
            self.arrPriority[biggerchild], self.arrPriority[idx] = self.arrPriority[idx], self.arrPriority[biggerchild]
            self.arrValue[biggerchild], self.arrValue[idx] = self.arrValue[idx], self.arrValue[biggerchild]
            self.percorlateDown(biggerchild)


    def dequeue(self):
        if self.size == 0:
            return ''
        #retPriority = self.arrPriority[0]
        retValue = self.arrValue[0]
        self.arrPriority[0] = self.arrPriority[self.size - 1]
        self.arrValue[0] = self.arrValue[self.size - 1]
        self.size -= 1
        self.percorlateDown(0)
        return retValue

    def build(self, arrInputPriority, arrInputValue):
        for i in range(len(arrInputPriority)):
            self.arrPriority[i] = arrInputPriority[i]
            self.arrValue[i] = arrInputValue[i]
        self.size = len(arrInputPriority)
        for j in range(self.size-1,-1,-1):
            self.percorlateDown(j)