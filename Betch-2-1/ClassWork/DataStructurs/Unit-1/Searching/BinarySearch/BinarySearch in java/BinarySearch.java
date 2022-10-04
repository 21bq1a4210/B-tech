import java.util.Scanner;
class BinarySearch {
    static int arr[],key;
    static Scanner sc=new Scanner(System.in);
    BinarySearch(){
        BinarySearch.read();
        BinarySearch.search();
    }
    private static void read(){
        System.out.print("enter no.of ele:");
        arr=new int[sc.nextInt()];
        System.out.print("enter elements:");
        for(int i=0;i<arr.length;i++){
            arr[i]=sc.nextInt();
        }
        System.out.print("enter key:");
        key=sc.nextInt();
    }
    private static void search(){
        int l=0;
        int h=arr.length-1;
        while(l<=h){
            int mid=(l+h)/2;
            if(key==arr[mid]){
                System.out.println("element found at:"+(mid+1));
                break;
            }
            else if(key>mid){
                l=mid+1;
            }
            else if(key<mid){
                h=mid-1;
            }
            else{
                System.out.println("element not found");
            }
        }
    } 

}

class Main{
    public static void main(String[] args) {
        BinarySearch bs=new BinarySearch();
    }
}

