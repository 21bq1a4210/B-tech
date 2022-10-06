class Exp4_int {
    public static void main(String[] args) {
        int a=1_2__3;
        //int b=_1_2_;  runtime error
        /*S
         Exception in thread "main" java.lang.Error: Unresolved compilation problem: 
        _1_2_ cannot be resolved to a variable
        at Exp4_int.main(Exp4_int.java:4)
         */
        System.out.println(a);  //123
        // Floating-point literals in Java default to double precision.
        float f1=6.022E23f, f3=2314159E05f;
        System.out.println(f1+" "+f3);  //6.022E23 2.31415906E11

        //Hexadecimal floating-point literals
        double h=0x12.2P2;
        System.out.println("h="+h); //72.5
        double num = 9_423_497.1_0_9;   
        System.out.println("num="+num); //9423497.109

    }
}
