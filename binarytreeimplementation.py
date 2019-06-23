class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class BST:
    def __init__(self):
        self.root=None
    def Insert(self,data):
        if self.root==None:
            self.root=Node(data)
            print(self.root.data)
            return
        else:
            self._Insert(data,self.root)
    def _Insert(self,data,currentnode):
        if data<currentnode.data:
            if currentnode.left is None:
                currentnode.left=Node(data)
            else:
                self._Insert(data,currentnode.left)
        elif data>currentnode.data:
            if currentnode.right is None:
                currentnode.right=Node(data)
            else:
                self._Insert(data,currentnode.right)
        else:
            print('Value already in the tree')
    def Display(self):
        if self.root!=None:
            self._Display(self.root)
    def _Display(self,cn):
        if cn!=None:
            self._Display(cn.left)
            print(str(cn.data))
            self._Display(cn.right)
def fill(tree,r=50,max=10000):
    from random import randint
    for i in range(r):
        element=randint(0,max)
        tree.Insert(element)
    return  tree
b=BST()
b=fill(b)
b.Display()
