import sys
import numpy as np

class BinaryExpressionTree:

    priorities = {"+":1, "-":1, "*":2, "/":2, "^":3, "(":0}
    unaryPriority = 4

    def __init__(self,line):
        tokens = line.split(" ")
        self.stackOperator = Stack()
        self.stackOperand = Stack()
        self.root = self.buildTree(tokens)
        print("Tokens : "+str(tokens))
        print("Prefix : " + self.traversPreFix())
        print("Postfix : " + self.traversPostFix())

    def buildTree(self,tokens):
        count_for = 0
        for itr in range(len(tokens)):
            token = tokens[itr]
            if token in self.priorities.keys():
                node = Node(token,self.priorities[token],False)
                if token == "(":
                    self.stackOperator.push(node)
                else:
                    if token == '-' and count_for >= self.stackOperand.length():
                        node.priority = self.unaryPriority
                        self.stackOperator.push(node)
                    else:
                        while self.stackOperator.top() != None and self.stackOperator.top().getPriority() >= node.getPriority():
                            if self.stackOperator.top().getPriority() != self.unaryPriority:
                                count_for = count_for - 1
                            self.mergeLastTwoOperand()
                        self.stackOperator.push(node)
                        count_for = count_for + 1
            elif token == ")": 
                while self.stackOperator.top().getValue() != "(":
                    self.mergeLastTwoOperand()
                    count_for = count_for - 1
                self.stackOperator.pop()
            elif token == 'ln':
                node = Node(token,self.unaryPriority,False)
                self.stackOperator.push(node)
            else:
                node = Node(token,-1,True)
                self.stackOperand.push(node)
            print("Step. " + str(itr + 1))
            print("Stack Operator : " + str(self.stackOperator))
            print("Stack Operand : " + str(self.stackOperand))
        while self.stackOperator.top() != None:
            self.mergeLastTwoOperand()
        return self.stackOperand.top()

    def evaluate(self, node = None):
        if node == None:
            node = self.root
        if node.getLeft() != None:
            valueLeft = self.evaluate(node.getLeft())
        if node.getRight() != None:
            valueRight = self.evaluate(node.getRight())
        if node.getLeft() != None and node.getRight() == None:
            if node.getValue() == '-':
                return float((-1)*valueLeft)
            elif node.getValue() == 'ln':
                return float(np.log(valueLeft))         
        elif node.getLeft() != None and node.getRight() != None:
            if node.getValue() == '+':
                return float(valueLeft + valueRight)
            elif node.getValue() == '-':
                return float(valueLeft - valueRight)
            elif node.getValue() == '*':
                return float(valueLeft * valueRight)
            elif node.getValue() == '/':
                return float(valueLeft / valueRight)
            elif node.getValue() == '^':
                return float(valueLeft ^ valueRight)
        else:
            return float(node.getValue())
            
    def __str__(self):
        return self.root.getString(0)

    def traversPreFix(self,node=None):
        if node == None:
            node = self.root
        ret = ""
        ret = ret + node.value
        if node.getLeft() != None:
            ret = ret + self.traversPreFix(node.getLeft())
        if node.getRight() != None:
            ret = ret + self.traversPreFix(node.getRight())	    
        return ret

    def traversPostFix(self,node=None):
        if node == None:
            node = self.root
        ret = ""
        if node.getLeft() != None:
            ret = ret + self.traversPostFix(node.getLeft())
        if node.getRight() != None:
            ret = ret + self.traversPostFix(node.getRight())
        ret = ret + node.value
        return ret

    def mergeLastTwoOperand(self):
        nodeOperator = self.stackOperator.pop()
        if nodeOperator.getPriority() == self.unaryPriority:
            Operand = self.stackOperand.pop()
            nodeOperator.setLeft(Operand)
            self.stackOperand.push(nodeOperator)
        else:
            Operand2 = self.stackOperand.pop()
            Operand1 = self.stackOperand.pop()
            nodeOperator.setLeft(Operand1)
            nodeOperator.setRight(Operand2)
            self.stackOperand.push(nodeOperator)

    def isDigit(self,token):
        try:
            float(token)
            return True
        except ValueError:
            return False

class Stack:
    def __init__(self):
        self.head = Node(None,-1,False,blnTop=True)
    def top(self):
        if self.head.getNext() != None:
            return self.head.getNext()
        return None
    def push(self,node):
        node.setNext(self.head.getNext())
        self.head.setNext(node)
    def pop(self):
        ret = self.head.getNext()
        if ret != None:
            self.head.setNext(ret.getNext())
        return ret
    def __str__(self):
        currentNode = self.head.getNext()
        ret = ""
        while currentNode != None:
            ret = str(currentNode.getValue()) + "," + ret
            currentNode = currentNode.getNext()
        return ret
    def length(self):
        cnt = 0
        node = self.head
        while node.getNext() != None:
            node = node.getNext()
            cnt = cnt+1
        return cnt
        

class Node:
    def __init__(self,value,priority,blnDigit,blnTop=False):
        self.value = value
        self.priority = priority
        self.blnTop = blnTop
        self.next = None
        self.left = None
        self.right = None
        self.blnDigit = None
    def isDigit(self):
        return self.blnDigit
    def getRight(self):
        return self.right
    def getLeft(self):
        return self.left
    def setRight(self,node):
        self.right = node
    def setLeft(self,node):
        self.left = node
    def setNext(self,node):
        self.next = node
    def getNext(self):
        return self.next
    def getValue(self):
        return self.value
    def getPriority(self):
        return self.priority
    def isTop(self):
        return self.blnTop
    def getString(self,depth):
        ret = ""
        for itr in range(depth):
            ret = ret + "...."
        ret = ret + str( self.getValue() ) + "\n"
        if self.getLeft() != None:
            ret = ret + self.getLeft().getString(depth+1)
        if self.getRight() != None:
            ret = ret + self.getRight().getString(depth + 1)
        return ret

if __name__ == "__main__":
    line = input("Enter formula : ")
    tree = BinaryExpressionTree(line)
    print ("Evaluate : "+str(tree.evaluate()))
    print ("Tree : \n"+str(tree))