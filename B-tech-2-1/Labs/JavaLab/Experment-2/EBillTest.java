package EBill;
//Welcome to EBillTest.java
import java.util.Scanner;//program uses class Scanner
public class EBillTest{//start of EBillTest class
	public static void main(String arr[]){// main method begins execution of Java application
		// create Scanner to obtain input from command window
		Scanner scan=new Scanner(System.in);
		
		System.out.print("enter consumer no:");//prompt
		String num=scan.nextLine();           //read a line of text
		
		System.out.print("enter consumer name:");//prompt
		String name=scan.nextLine();            //read a line of text
		
		System.out.print("enter previous month reading:");//prompt
		double pr=scan.nextDouble();          //read a double
		
		System.out.print("enter current month reading:");//prompt
		double cr=scan.nextDouble();           //read a double 
		
		// create a EBill object and assign it to eb1
		EBill eb1=new EBill(num,name,pr,cr);
		
		System.out.print("1.domestic\n2.commercial\ntype of EB connection:");//prompt
		int choice=scan.nextInt();              //read a int
		scan.close();
		System.out.println("consumer no:"+eb1.consumer_no);//display initial data of the consumer number
		System.out.println("consumer name"+eb1.consumer_name);//display nitial data of the consumer name
		if (choice==1) System.out.print("the total amount:"+eb1.domestic());//display initial data of the total amount for domestic
		else System.out.print("the total amount:"+eb1.commercial());//display initial data of the total amount for commercial
	}//end of main method
};//end of EBillTest class
