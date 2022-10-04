import java.util.Scanner;
class InsertionSort{
    private static int arr[];
    static Scanner sc=new Scanner(System.in);

    InsertionSort(){
        read();
        sort();
        display();
    }

    private static void read(){
        System.out.print("enter no.of elements:");
        arr=new int[sc.nextInt()];
        System.out.print("enter elements:");
        for(int i=0;i<arr.length;i++){
            arr[i]=sc.nextInt();
        }
    }

    private static void sort(){
        for(int i=0;i<arr.length;i++){
            int j=i-1;
            int temp=arr[i];
            while(j>=0 && temp<arr[j]){
                arr[j+1]=arr[j];
                j-=1;
            }arr[j+1]=temp;
        }
    }
    
    private static void display(){
        System.out.print("sorted array:");
        for(int i=0;i<arr.length;i++){
            System.out.print(arr[i]+" ");
        }
    }
}

class Main{
    public static void main(String[] args) {
        InsertionSort is=new InsertionSort();
    }
}