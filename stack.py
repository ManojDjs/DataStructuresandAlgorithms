stack=[]
class Stack:
    def __init__(self,data):
        self.data=data
    def Insert(data):
        if len(stack)>10:
            print("Stack Over Flow") #for stack overflow condition
        else:
            stack.append(data)
    def Remove(self):
        if(len(stack)==0):
            print("Stack Underflow , Cannot remove Values")
        else:
            k=stack.pop()
            print(k+ "is Removed from the Stack")
k=Stack
print("Welcome to stack:: ")
choice=1
while choice<4:
    print('operations to be performed:')
    print("1.Insert\n 2.Remove \n 3.Show Stack \n 4. enter 0 for exit")
    choice=int(input("Enter your choice:\n"))
    if choice==1:
        k.Insert(input('enter data to enter'))
    elif choice==2:
        k.Remove(choice)
    elif choice==3:
        print(stack)
    else:
        quit()


