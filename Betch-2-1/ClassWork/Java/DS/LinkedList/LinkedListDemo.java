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
	public static void main(String[] args)
	{
		LinkedList llist = new LinkedList();    //creating the linkedlist obj

		llist.head = new Node(1);  
		Node second = new Node(2);
		Node third = new Node(3);

		llist.head.next = second; 

		second.next = third; 
        llist.print();
	}
}
