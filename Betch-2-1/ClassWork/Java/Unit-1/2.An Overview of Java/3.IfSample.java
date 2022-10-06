public class IfSample {
/*
    Demonstrate the if.
    Call this file "IfSample.java".
*/
    public static void main(String args[]) {
    int x, y;
    x = 10;
    y = 20;
    if(x < y) System.out.println("x="+x+" is less than y="+y); // 10<20
    x = x * 2;  //20
    if(x == y) System.out.println("x="+x+" now equal to y"+y);  // 20=20
    x = x * 2;  //  40
    if(x > y) System.out.println("x="+x+" now greater than y"+y); //40>20 
    // this won't display anything
    if(x == y) System.out.println("you won't see this");
    }
};

