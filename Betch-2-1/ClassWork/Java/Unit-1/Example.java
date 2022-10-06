/*
 * this is a sample program.
   call this as "Example.java"
 */
public class Example {
    //program begins with a call main() "single line comment"
    public static void main(String[] args) {
        /*
         * the "public" keyword is an access modifier, which allows the programmer to control the
visibility of class members.

         * the keyword "static" allows main( ) to be called without 
having to instantiate a particular instance of the class. This is necessary since main( ) is
called by the Java Virtual Machine before any objects are made.

         *the keyword "void" simply
tells the compiler that main( ) does not return a value.

         *String args[ ] declares a parameter named args, which is an array of instances of the class
String. (Arrays are collections of similar objects.) Objects of type String store character
strings. In this case, args receives any command-line arguments present when the program
is executed.

         *main( ) is simply a starting place for your program. A complex
program will have dozens of classes, only one of which will need to have a main( ) method
to get things started.
         */
        System.out.println("My first program in java ^(@_@)^");
        /*
         * System is a predefined final class that provides access to the system,
and out is the output stream that is connected to the console.
         * the println methods in class PrintStream.
         */
    }   
    
}
