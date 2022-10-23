class LinkedList {  // linkedlist main class
	Node head;  // head of the node 
	static class Node { // node class
		int data;   // instance varable of integer type
		Node next;  // instance varable of Node type
		Node(int d) {   //constructor of node
			data = d;   //data inistalazaton
			next = null;    //reference varable
		} 
	}
    public void print(){ //to print the linked list
        Node temp = head;   //starting point of the node
        while(temp!=null){  //checking for the condition
            System.out.print(temp.data+" "); //printing the data
            temp=temp.next; //changing the refrence data
        }
    }
    public void append(int new_data){
        Node new_node=new Node(new_data);
        if(head == null){
            head=new Node(new_data);
        }
        else{
            Node last=head;
            while(last.next!=null){
                last=last.next;
            }
            last.next=new_node;
        }
    }
	public static void main(String[] args)
	{
		LinkedList llist = new LinkedList();    //creating the linkedlist obj
        llist.append(10);
        llist.append(20);
        llist.append(30);
        llist.print();
	}
}
