package Book;
//Welcome to BookTest.java
import java.util.Scanner;//program uses class Scanner
class BookTest{//start of the BookTest class
    public static void main(String args[]){//main method begins execution of Java application
        Book[] obj=new Book[30];//creating an array of objects
        Scanner scan=new Scanner(System.in);// create Scanner to obtain input from command window

        System.out.print("enter no.of books:");//prompt
        int n=scan.nextInt();//read a int

        for(int i=0;i<n;i++){//start of for loop
            System.out.println("\nenter details of book:");//prompt
            obj[i]=new Book();//create a Book object and assign it to obj array

            System.out.print("enter book name:");//prompt
            String name=scan.next();//read a line of text
            obj[i].setName(name);//set the name of the book 

            System.out.print("enter book ISBN:");//prompt
            int ISBN= scan.nextInt();//read a int
            obj[i].setISBN(ISBN);//set the ISBN of the book

            System.out.print("enter book author:");//prompt
            String aut=scan.next();//read a line of text
            obj[i].setAuthor(aut);//set the author name of the book

            System.out.print("enter book publisher:");//prompt
            String publisher=scan.next();///read a line of text
            scan.close();
            obj[i].setPublisher(publisher);//set the author publisher of the book
        }//end of for loop

        for(int i=0;i<n;i++){//start of the for loop
            System.out.println("\nBook:"+(i+1));//prompt
            obj[i].getBookInfo();//dsiplying the book description
        }//end of the for loop
        
    }//end of main method
};//end the BookTest class
