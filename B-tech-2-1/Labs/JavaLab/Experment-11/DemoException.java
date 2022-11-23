import java.util.InputMismatchException;
import java.util.Scanner;
class DemoException{
    public static void main(String[] args) {
        try{
            Scanner input=new Scanner(System.in);
            System.out.print("Enter numerator and denominator:");
            int numerator=input.nextInt();
            int denominator=input.nextInt();
            input.close();
            float c=numerator/denominator;
            System.out.println("Result:"+c);
        }catch(InputMismatchException e){
            System.out.println("Invalid input:");
            e.printStackTrace();
        }catch(ArithmeticException e){
            System.out.println("Arithmetic error:");
            e.printStackTrace();
        }catch(Exception e){
            System.out.println("Error found:");
            e.printStackTrace();
        }
    }
}