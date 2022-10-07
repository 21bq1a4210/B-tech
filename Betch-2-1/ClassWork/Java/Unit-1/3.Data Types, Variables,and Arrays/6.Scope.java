// Demonstrate block scope.
class Scope {// scope "a" start here
    static int a=100;
    public static void main(String args[]) {// known to all code within main
    int x; // let say scope "x" start here
    x = 10;
    if(x == 10 && a==100) { // start new scope of "y"
    int y = 20; // known only to this block
    // x and y both known here.
    System.out.println("x, y and a: " + x + " " + y+" "+a);
    x = y * 2;
    a/=2;
    }// end of scope of "y"
    // y = 100; // Error! y not known here
    // x is still known here.
    System.out.println("x and a is " + x+" "+a);
    } //end of scope of "x"
};// end of scope of "a"