class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:     #PYTHON LINKED LIST WITH OPERATIONS
    def __init__(self):
        self.head=None
    def Insert(self,data):
        temp=Node(data)
        if self.head is None:
            self.head=temp
            return
        CurrentNode=self.head
        while CurrentNode.next:
            CurrentNode=CurrentNode.next
        CurrentNode.next=temp
    def Atstart(self,data):
        temp=Node(data)
        temp.next=self.head
        self.head=temp
    def Inbetween(self,elementafter,data):
        newNode=Node(data)
        newNode.next=elementafter.next
        elementafter.next=newNode
    def Display(self):
        CurrentNode=self.head
        while CurrentNode is not None:
                print(CurrentNode.data)
                CurrentNode=CurrentNode.next
    def Delete(self,key):
        currentnode=self.head
        if currentnode.data==key:
            self.head=currentnode.next
            currentnode.next=None
            return
        while currentnode and currentnode.data !=key:
            previousnode=currentnode
            currentnode=currentnode.next
        if currentnode is None:
                return
        previousnode.next=currentnode.next
        currentnode=None

l=LinkedList()
while choice<=4:
    print('operations to be performed:')
    print("1.Insert at begining \n2.AT begining \n3.Remove \n 4.Show Linked List \n 5. enter 5 for exit")
    choice=int(input("Enter your choice:\n"))
    if choice==1:
        l.Insert(input('enter data to enter'))
    elif choice==2:
        l.Delete(choice)
    elif choice==3:
        l.Display()
    else:
        quit()

l.Insert(3)
l.Atstart(1)
l.Insert(2)
l.Inbetween(l.head.next,5)
l.Inbetween(l.head.next,8)
l.Display()
l.Delete(5)
l.Display()
