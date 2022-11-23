import java.io.*;
// Demonstrate char data type.
class CharDemo {
    public static void main(String args[]) {
    char ch1;
    ch1 = 88; // code for X
    System.out.print("ch1="+ch1+", hase code=");
    System.out.println(System.identityHashCode(ch1));   //1523554304
    ch1 = 'Y';
    System.out.print("ch1="+ch1+", hase code=");
    System.out.println(System.identityHashCode(ch1));   //1175962212
    // both are different
    }
}