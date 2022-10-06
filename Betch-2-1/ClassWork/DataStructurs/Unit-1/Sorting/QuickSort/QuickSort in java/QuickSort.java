import java.util.Scanner;
class QuickSort {
    private static int arr[];
    static Scanner sc=new Scanner(System.in);

    QuickSort(){
        read();
        quickSort(arr, 0, arr.length-1);
        print();
    }

    private static void read(){
        System.out.print("enter no.of elements:");
        arr=new int[sc.nextInt()];
        System.out.print("enter elements:");
        for(int i=0;i<arr.length;i++){
            arr[i]=sc.nextInt();
        }
    }

    private static int partiton(int arr[],int low,int high){
        int pivot=arr[high];
        int i =low-1;
        for(int j=low;j<high;j++){
            if(arr[j]<=pivot){
                i+=1;
                int temp= arr[i];
                arr[i]=arr[j];
                arr[j]=temp;
            }
        }
        int temp=arr[i+1];
        arr[i+1]=arr[high];
        arr[high]=temp;
        return i+1;
    }

    private static void quickSort(int arr[],int low, int high){
        if(low<high){
            int pi=partiton(arr, low, high);
            quickSort(arr, low, pi-1);
            quickSort(arr, pi+1, high);
        }
    }

    private static void print(){
        System.out.print("sorted array:");
        for(int i=0;i<arr.length;i++){
            System.out.print(arr[i]+" ");
        }
    }
}

class Main{
    public static void main(String[] args) {
        QuickSort qs = new QuickSort();
    }
}