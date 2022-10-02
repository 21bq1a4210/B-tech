package Invoice;
//Welcome to InvoiceTest.java
import java.util.Scanner; //program uses class Scanner
public class InvoiceTest{
	public static void main(String arr[]){// main method begins execution of Java application
		// create a Invoice object and assign it to ob1
		Invoice ob1=new Invoice();
		// create Scanner to obtain input from command window
		Scanner scan=new Scanner(System.in);

		System.out.print("Enter system number:");//prompt
		String num=scan.nextLine();             //read a line of text
		ob1.setNumber(num);                    //set the item number
		
		System.out.print("Enter system descriptions:");//prompt
		String des=scan.nextLine();                   //read a line of text
		ob1.setDescription(des);                     //set the item description 
		
		System.out.print("Enter system quantity:");//prompt
		int qua=scan.nextInt();			  //read a integer
		ob1.setQuantity(qua);			 //set the item quantity 
		


		System.out.print("Enter system prise:");//prompt
		double pri=scan.nextDouble();          //read a double
		ob1.setPrise(pri);                    //set the ite prise
		scan.close();

		System.out.println("Item number:"+ob1.getNumber()); // display initial data of item number
		System.out.println("Item description:"+ob1.getDescription ()); // display initial data of item description
		System.out.println("Item quantity:"+ob1.getQuantity());  // display initial data of item quantity 
		System.out.println("Item prise:"+ob1.getPrise());	//display initial data of the item prise
		System.out.println("Total prise:"+ob1.getInvoiceAmount());//display initial data of the total rise
		
	}//ending of main method
};//ending of InvoiceTest class
