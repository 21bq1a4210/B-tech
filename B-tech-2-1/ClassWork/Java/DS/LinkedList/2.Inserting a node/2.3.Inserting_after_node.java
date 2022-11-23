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
    public void push(int new_data){
        Node new_node = new Node(new_data);
        new_node.next=head;
        head=new_node;

    }
    public void print(){ //to print the linked list
        Node temp = head;   //starting point of the node
        while(temp!=null){  //checking for the condition
            System.out.print(temp.data+" "); //printing the data
            temp=temp.next; //changing the refrence data
        }
    }
    public void addAfter(int new_data,int data){
        Node temp=head;
        while(temp!=null && temp.data==data){
                Node new_node=new Node(new_data);
                new_node.next=temp.next;
                temp.next=new_node;
                break;
        }
        
    }
    
	public static void main(String[] args)
	{
		LinkedList llist = new LinkedList();    //creating the linkedlist obj
        llist.push(1);
        llist.push(3);
        llist.addAfter(2,3 );
        llist.push(4);
        llist.print();
	}
}
