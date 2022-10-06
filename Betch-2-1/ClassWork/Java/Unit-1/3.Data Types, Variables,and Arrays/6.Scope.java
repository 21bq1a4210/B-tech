// Demonstrate block scope.
class Scope {
    static int a=100;
    public static void main(String args[]) {
    int x; // known to all code within main
    x = 10;
    if(x == 10 && a==100) { // start new scope
    int y = 20; // known only to this block
    // x and y both known here.
    System.out.println("x, y and a: " + x + " " + y+" "+a);
    x = y * 2;
    a/=2;
    }
    // y = 100; // Error! y not known here
    // x is still known here.
    System.out.println("x and a is " + x+" "+a);
    }
};