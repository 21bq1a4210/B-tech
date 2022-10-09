import java.util.Scanner;
class Employee{
    String Emp_name;
    int Emp_id;
    String Address;
    String Mail_id;
    int Mobile_no;
    public void read(){
        Scanner sc=new Scanner(System.in);
        System.out.print("enter the emp name:");
        Emp_name=sc.next();
        System.out.print("enter the emp id:");
        Emp_id=sc.nextInt();
        System.out.print("enter the emp adderss:");
        Address=sc.next();
        System.out.print("enter the emp mail:");
        Mail_id=sc.next();
        System.out.print("enter the emp moblie.no:");
        Mobile_no=sc.nextInt();
    }
    public void empDisplay(){
        System.out.println();
        System.out.println("emp name: "+Emp_name);
        System.out.println("emp id: "+Emp_id);
        System.out.println("emp address: "+Address);
        System.out.println("emp mail: "+Mail_id);
        System.out.println("emp mobile.no: "+Mobile_no);
        System.out.println();
    }
};

class Programmer extends Employee{  
    private double BP; 
    Programmer(double BP){
        this.BP=BP;
    }
    void display(){
        System.out.println("BP:"+BP);
        System.out.println("DA:"+0.97*BP);
        System.out.println("HRA:"+0.10*BP);
        System.out.println("PF:"+0.12*BP);
        System.out.println("SATFF CLUD FUND:"+0.001*BP);  
        System.out.println("Gross sal:"+((2.191)*BP));
        System.out.println("Net sal:"+((2.07)*BP)); 
        System.out.println(); 
    }
} 
class Assistant_Professor extends Employee{  
    private double BP;
    Assistant_Professor(double BP){
        this.BP=BP;
    }
    void display(){

        System.out.println("BP:"+BP);
        System.out.println("DA:"+0.97*BP);
        System.out.println("HRA:"+0.10*BP);
        System.out.println("PF:"+0.12*BP);
        System.out.println("SATFF CLUD FUND:"+0.001*BP);
        System.out.println("Gross sal:"+((2.191)*BP));
        System.out.println("Net sal:"+((2.07)*BP));  
        System.out.println();
    }
} 
class Associate_Professor extends Employee{  
    private double BP;
    Associate_Professor(double BP){
        this.BP=BP;
    }
    void display(){

        System.out.println("BP:"+BP);
        System.out.println("DA:"+0.97*BP);
        System.out.println("HRA:"+0.10*BP);
        System.out.println("PF:"+0.12*BP);
        System.out.println("SATFF CLUD FUND:"+0.001*BP);
        System.out.println("Gross sal:"+((2.191)*BP));
        System.out.println("Net sal:"+((2.07)*BP)); 
        System.out.println(); 
    }
} 
class Professor extends Employee{  
    private double BP;
    Professor(double BP){
        this.BP=BP;
    }
    void display(){

        System.out.println("BP:"+BP);
        System.out.println("DA:"+0.97*BP);
        System.out.println("HRA:"+0.10*BP);
        System.out.println("PF:"+0.12*BP);
        System.out.println("SATFF CLUD FUND:"+0.001*BP);
        System.out.println("Gross sal:"+((2.191)*BP));
        System.out.println("Net sal:"+((2.07)*BP));  
        System.out.println();
    }
} 
class Main{ 
public static void main(String args[]){
    System.out.println("\n 1.Programmer\n2.Assistant_Professor\n3.Associate_Professor\n4.Professor");
    Scanner input=new Scanner(System.in);
    System.out.print("Enter your option(1 to 4):");
    int op=input.nextInt();
    switch (op) {
        case 1:
           Programmer p=new Programmer(15000);
           p.read();
           p.empDisplay();
           p.display();
           break;
        case 2:
           Assistant_Professor assp=new Assistant_Professor(45_000);
           assp.read();
           assp.empDisplay();
           assp.display();
           break;
        case 3:
           Associate_Professor ap=new Associate_Professor(75_000);
           ap.read();
           ap.empDisplay();
           ap.display();
           break;
        case 4:
           Professor pro=new Professor(1_00_000);
           pro.read();
           pro.empDisplay();
           pro.display();
           break;
         default: 
          System.out.println("enter correct choice");
        } 
    }
}