// This program will not compile
class ScopeErr {
    public static void main(String args[]) {
    int bar = 1;
        { // creates a new scope
        int bar = 2; // Compile-time error – bar already defined!
        /*
        Exception in thread "main" java.lang.Error: Unresolved compilation problem: 
        Duplicate local variable bar
        at ScopeErr.main(ScopeErr.java:6) 
         */
        }
    }
};