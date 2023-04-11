import Prim
import Graph
import NetworkClustering
import csv
import Tree

def Treebalancing(tree):
    currentDepth = tree.findMaxDepth(tree.head)
    
    while True:
        maxSubDepth = -999
        childMaxSubDepth = None
        for child in tree.head.children:
            if tree.findMaxDepth(child) > maxSubDepth:
                maxSubDepth = tree.findMaxDepth(child)
                childMaxSubDepth = child
                
        tree.head.remove(childMaxSubDepth)
        childMaxSubDepth.addchild(tree.head)
        tree.head.weight = childMaxSubDepth.weight
        childMaxSubDepth.weight = 0
        
        newDepth = tree.findMaxDepth(childMaxSubDepth)
        if newDepth >= currentDepth:
            tree.head.addchild(childMaxSubDepth)
            childMaxSubDepth.weight = tree.head.weight
            tree.head.weight = 0
            childMaxSubDepth.remove(tree.head)
            break
        else:
            tree.head = childMaxSubDepth
    
    return tree
    
if __name__ == "__main__":
    g = Graph.DenseGraph('Subway-Seoul-ver-2.csv')
    #g = Graph.DenseGraph('Subway-Seoul.csv')
    num_hubstantion = 10
    clustering = NewmanClustering()
    components = clustering.performNewmanClustering(g,num_hubstantion)
    print('아놔', components)
    components_copy=[]
    for i in range(len(components)):
        tmp=[]
        for j in range(len(components)):
            tmp.append(components[i][j])
        components_copy.append(tmp)
        
    components_Tree = []
    for itr in range(len(components)):
        component = components[itr]
        a = Tree()
        a.head = Node(component[0])
        for vertex in component:
            if vertex in g.edges[component[0]]:
                a.head.addchild(Node(vertex, g.edges[a.head][vertex]))
                
        component.remove(component[0])
        for child in a.head.children:
            component.remove(child)
            while True:
                tmp = 0
                for vertex in component:
                    if vertex in g.edges[child]:
                        child.addchild(Node(vertex, g.edges[child][vertex]))
                        component.remove(vertex)
                        tmp = 1
                if tmp == 0 :
                    break
                
        components_Tree.append(a)
        
    components = components_copy
    tree_list=[]
    for tree in components_Tree:
        new_tree = Treebalancing(tree)
        tree_list.append(new_tree)
        
    for itr in range(len(components)):
        print(itr+1,'. Component of', components[itr])
        print('Local Supply Tree')
        tree_list[itr].printTree(tree_list[itr].head)