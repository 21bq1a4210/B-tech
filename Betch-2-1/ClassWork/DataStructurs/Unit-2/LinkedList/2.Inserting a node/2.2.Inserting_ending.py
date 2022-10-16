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
    def append(self,new_data):#1line
        #step 1: Create a new node
        #step 2: Put in the data
        #step 3: Set next as None
        new_node=Node(new_data)#2line
        #step 4: If the LL is empty, then make the new node as head
        if self.head is None:#3line
            self.head=Node(new_data)#4line
        #step 5: Else traverse till the lat node
        last=self.head#5line
        while last.next:#6line
            last=last.next#7line
        #step 6: Change the next of last node
        last.next=new_node#8line
        '''
        In the 2st line we are creating a NewNode using Node class
        In the 3nd line we are checking for the condition whether the linledlist\
                    is created or not. if LL is not created the it is the 1st Node\
                    which should have head
        In the 5th line we are creating a last varable which is pointing to the new\
                    of head
        In the 6th line we are travicing until the last.next is None
        In the 8th line we are linking the address of new_node to the LastNode which consisit of\
                    None in ref.
        '''
if __name__=="__main__":
    ll1=LinkedList()
    ll1.head=Node(1)
    N2=Node(2)
    N3=Node(3)
    ll1.head.next=N2
    N2.next=N3
    ll1.print()#1 2 3
    ll1.append(0)
    print()#\n
    ll1.print()#1 2 3 0
    print()#\n
    ll1.append(-1)
    ll1.print()#1 2 3 0 -1
