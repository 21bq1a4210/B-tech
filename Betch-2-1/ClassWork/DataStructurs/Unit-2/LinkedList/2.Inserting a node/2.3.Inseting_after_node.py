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
            
    def addAfter(self,new_data,pre_node):
        if pre_node is None:
            print("the previous is not linked")
            return
        next_pre_node=pre_node.next
        new_data=Node(new_data)
        pre_node.next=new_data
        new_data.next=next_pre_node
        
if __name__=="__main__":
    ll1=LinkedList()
    N1=Node(1)
    ll1.head=N1
    N2=Node(2)
    N3=Node(3)
    ll1.head.next=N2
    N2.next=N3

    ll1.addAfter(1.5,N2)
    ll1.print()
    print()
    ll1.addAfter(True,N1)
    ll1.print()
    
    
