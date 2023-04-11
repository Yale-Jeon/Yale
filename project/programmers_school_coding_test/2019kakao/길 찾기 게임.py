class Tree:
    def __init__(self):
        self.head = ''

    def insert(self, value, num, node=''):
        if node == '':
            node = self.head
        if self.head == '':
            self.head = Node(value, num)
            return

        if value < node.value:
            if node.hasleft():
                self.insert(value, num, node.leftchild)
            else:
                node.leftchild = Node(value, num)
        else:
            if node.hasright():
                self.insert(value, num, node.rightchild)
            else:
                node.rightchild = Node(value, num)

    def preorder(self, node):
        answer = [node.num]
        if node.hasleft():
            answer += self.preorder(node.leftchild)
        if node.hasright():
            answer += self.preorder(node.rightchild)
        return answer

    def postorder(self, node):
        answer = []
        if node.hasleft():
            answer += self.postorder(node.leftchild)
        if node.hasright():
            answer += self.postorder(node.rightchild)
        answer.append(node.num)
        return answer


class Node:
    def __init__(self, value, num):
        self.num = num
        self.value = value
        self.leftchild = ''
        self.rightchild = ''

    def hasleft(self):
        if self.leftchild != '':
            return True
        return False

    def hasright(self):
        if self.rightchild != '':
            return True
        return False


def solution(nodeinfo):
    answer = []
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i+1)

    nodeinfo = sorted(nodeinfo, key=lambda x: x[1], reverse=True)
    tree = Tree()

    for i in range(len(nodeinfo)):
        tree.insert(nodeinfo[i][0:1],nodeinfo[i][-1])

    pre = tree.preorder(tree.head)
    post = tree.postorder(tree.head)

    answer.append(pre)
    answer.append(post)
    return answer