import java.util.Scanner; //program uses class Scanner
class BinarySearch { //start of the BinarySearch class
    static int arr[],key; //static instance varables
    static Scanner sc=new Scanner(System.in); //create Scanner to obtain input from command window
    BinarySearch(){ //start of the constructor
        read(); //calling read method of same class
        search();// calling search method of same class
    }
    private static void read(){ //start of private static method read
        System.out.print("enter no.of ele:"); //promt
        arr=new int[sc.nextInt()]; //allocating memoery
        System.out.print("enter elements:"); //promt
        for(int i=0;i<arr.length;i++){ //start of for loop
            arr[i]=sc.nextInt();// appending element from the keyboard
        }//end of the for loop
        System.out.print("enter key:"); //promt
        key=sc.nextInt(); //reading a int
    }//end of method

    private static void search(){ //start of search method
        int l=0; //local varable
        int h=arr.length-1; //loca varable
        while(l<=h){ //start of while loop
            int mid=(l+h)/2; 
            if(key==arr[mid]){ //checking for condition
                System.out.println("element found at:"+(mid+1)); //promt
                break; // if condition statifies break from the loop
            }
            else if(key>mid){
                l=mid+1; //change low value
            }
            else if(key<mid){
                h=mid-1; //change high value
            }
            else{
                System.out.println("element not found");
            }
        }
    } 

};

class Main{ //start of main class
    public static void main(String[] args) { //start main method
        BinarySearch bs=new BinarySearch(); //create a BinarySearch object and assign it to bs
    } //end of main method
}; //end of class

