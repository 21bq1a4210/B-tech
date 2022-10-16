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
    #Function used to insert a new node at the beginning
    def push(self,new_data):#1line
        #step 1&2: Allocate the Node &
        #      Put in the data
        new_node=Node(new_data)#2line
        #step 3: Make next of new Node as head
        new_node.next=self.head#3line
        #step 4: Move the head to ref to new Node
        self.head=new_node#4line
        """
        In the 2nd line of the method we are creating a new node using Node class
        In the 3rd line we are assining the data address of the N1 to New_Node/
        i.e there is b/w N1 and New_Node
        In the 4th line we are assining the address of New_Node to head
        finally the new node has it head along with the address of next node i.e N1
        """
if __name__=="__main__":
    ll1=LinkedList()
    ll1.head=Node(1)
    N2=Node(2)
    N3=Node(3)
    ll1.head.next=N2
    N2.next=N3
    ll1.print()
ll1.push(0)
print()
ll1.print()
print()
ll1.push(-1)
ll1.print()
