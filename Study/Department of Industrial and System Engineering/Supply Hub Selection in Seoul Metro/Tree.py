class Node:
    def __init__(self, value=None, weight=0):
        self.children = []
        self.value = value
        self.weight = weight
    def setvalue(self, new_value):
        self.value = new_value
    def addchild(self, child):
        self.children.append(child)
    def removechild(self, child):
        self.children.remove(child)
    def empty(self):
        if len(self.children.keys()) == 0:
            return True
        else:
            return False
        
class Tree:
    def __init(self, head=None):
        self.head = head
    def findMaxDepth(self, node=None):
        Depth = 0
        subDepth = []
        if not node.empty():
            for child in node.children:
                depth = child.weight + self.findMaxDepth(child)
                subDepth.append(depth)
            Depth = max(subDepth)
        
        return Depth
    def printTree(self, node, tmp=0):
        print('....'*tmp + node.value)
        tmp = tmp+1
        for child in node.children:
            self.printTree(child, tmp)