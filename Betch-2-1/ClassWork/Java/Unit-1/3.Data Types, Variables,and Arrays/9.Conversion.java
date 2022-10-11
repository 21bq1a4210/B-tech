// Demonstrate casts.
class Conversion {
    public static void main(String args[]) {
    byte b;
    int i = 257;
    double d = 323.142;
    System.out.println("\nConversion of int to byte.");
    b = (byte) i;
    System.out.println("i and b " + i + " " + b);   // i and b 257 1
    System.out.println("\nConversion of double to int.");
    i = (int) d;
    System.out.println("d and i " + d + " " + i);   // d and i 323.142 323
    System.out.println("\nConversion of double to byte.");
    b = (byte) d;
    System.out.println("d and b " + d + " " + b);   // d and b 323.142 67
    }
    /*
     * When the value 257 is cast into a byte variable, the result is the
    remainder of the division of 257 by 256 (the range of a byte), which is 1 in this case. When
    the d is converted to an int, its fractional component is lost. When d is converted to a byte, its
    fractional component is lost, and the value is reduced modulo 256, which in this case is 67.
     */
};