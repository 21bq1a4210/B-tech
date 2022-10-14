class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None        
    def print(self):
        temp=self.head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
    def append(self,new_data):#1
        new_node=Node(new_data)#2
        if self.head is None:
            self.head=Node(new_data)
        last=self.head
        while last.next:
            last=last.next
        last.next=new_node
if __name__=="__main__":
    ll1=LinkedList()
    ll1.head=Node(1)
    N2=Node(2)
    N3=Node(3)
    ll1.head.next=N2
    N2.next=N3
    ll1.print()#\n
    ll1.append(0)
    print()#\n
    ll1.print()#1 2 3 0
    print()#\n
    ll1.append(-1)
    ll1.print()#1 2 3 0 -1
