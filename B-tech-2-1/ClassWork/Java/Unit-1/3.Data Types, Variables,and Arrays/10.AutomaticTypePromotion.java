class AutomaticTypePromotion{
    public static void main(String[] args) {
        byte a = 40;
        byte b = 50;
        int d = a * b;/*easily exceeds the range of either of its byte operands.
        *the subexpression a*b is performed using integers—not bytes.
        */
        //Java automatically promotes each byte, short,or char operand to int when evaluating an expression
        System.out.println(d);//2000

        /*
        Code:
         b = b * 2;
         System.out.println(b);

        Exception:
         Exception in thread "main" java.lang.Error: Unresolved compilation problem: 
         Type mismatch: cannot convert from int to byte
         at AutomaticTypePromotion.main(10.AutomaticTypePromotion.java:11)

        Explanation:
         the subexpresion b*2 is performed using int which is automatic an int cant 
         assigned to a byte without the use of a cast.
         */
        //solution:

         b = (byte) (b * 2);    // byte should be int ()
         /*we are explectuly converting b*2 which is in int to byte
         b=b*(byte)(2);  the same error will generate as above         
         */
         System.out.println(b); //100
    }
}