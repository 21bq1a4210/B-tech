import java.math.PI; //use of PI
import java.util.Scanner;   //use to read input
class AreaOfCircle {
    public static void main(String[] args) {
        System.out.print("enter the radius of circle:");
        Scanner sc=new Scanner(System.in);
        double radius=sc.nextDouble();
        double area= Math.PI*radius*radius;
        System.out.println("the value of pi in math class:"+Math.PI);
        System.out.println("the area of circle :"+area);
        sc.close();
    }
}
