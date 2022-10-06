class Exp3_BoolTest {
    public static void main(String[] args) {
        int a=1, b=0;
        //if(a) System.out.println("a is non-zero and it is true");
        /*
          Exception in thread "main" java.lang.Error: Unresolved compilation problem:
        Type mismatch: cannot convert from int to boolean
        at Exp3_BoolTest.main(Exp3_BoolTest.java:4)
         */
        System.out.println("10>9:"+(10>9));
        System.out.println("10<9:"+(10<9));
        System.out.println("10==10:"+(10==10));
        
        //System.out.println("char a and string a"+('a'=="a"));
        /*Exception in thread "main" java.lang.Error: Unresolved compilation problem: 
        Incompatible operand types char and String

        at Exp3_BoolTest.main(Exp3_BoolTest.java:15)
        */
    }
}
