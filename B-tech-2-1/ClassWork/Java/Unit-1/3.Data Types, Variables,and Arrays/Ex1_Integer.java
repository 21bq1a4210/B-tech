public class Ex1_Integer{
   public static void main(String[] args) {
    int i = 2147483647, o=0143, h=0x8f; //o,h are octal and hexa decimal
    float f = 10.143f; //"f" must placed else you will find a Error (double)
    double d = 10.143;
    short s = 32767;    //max value of short
    byte b = 127;   //max valu of byte
    System.out.println("float f="+f);
    System.out.println("double d="+d);
    System.out.printf("int i=%d, o=%d, h=%d\n",i,o,h);
    System.out.println("short s="+s);
    System.out.println("byte b="+b);

    System.out.println();
    i+=2;
    o+=2;
    h+=2;
    s+=2;
    b+=2;
    
    System.out.println("float f="+f);
    System.out.println("double d="+d);
    System.out.printf("int i=%d, o=%d, h=%d\n",i,o,h);  //int i=-2147483647, o=101, h=145
    System.out.println("short s="+s);   //short s=-32767
    System.out.println("byte b="+b);    //byte b=-127Quintonboy1
   }
}
