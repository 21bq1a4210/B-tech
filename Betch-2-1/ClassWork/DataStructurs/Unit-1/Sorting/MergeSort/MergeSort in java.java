import java.util.Scanner;//program uses class Scanner
class MergeSort{//start of MergeSort class

    public void mergeSort(int a[], int low,int high){//start of mergeSort method (Dividing into sub arr)
        int mid;//local varable
        if(low<high){//check for condition
            mid=(low+high)/2;
            mergeSort(a,low,mid);
            mergeSort(a,mid+1,high);
            merge(a,low,mid,high);
        }//end of if block
    }  //end of mergeSort method 

    private void merge(int arr[],int low,int mid, int high){//start of merge meythod (Meargeing of arr alog with sort)
        int i=low,j=mid+1,k=0;//loccal varables
        int b[]=new int[arr.length];//creating new arrays

        while(i<=mid && j<=high){//start of while loop block (comapring 2 arrs)
            if(arr[i]<=arr[j]){//start of if block
                b[k++]=arr[i++];
            }//end of if block
            else{//start of else block
                b[k++]=arr[j++];
            }//end of else block
        }
            
        while(i<=mid){//start of while loop block (adding remaing ele)
            b[k++]=arr[i++];
        }//end while loop block

        while(j<=high){//start of while loop block (adding remaing ele)
            b[k++]=arr[j++];
        }//end of while loop block
    
        k=0;
        for(i=low;i<=high;i++){//start of for loop (adding ele to original arr)
            arr[i]=b[k++];
        }//end of for loop
           
    }//end of merge method
   
};


class Main{//start of main class
    public static void main(String [] args) {//start of main method
      int a[],n;//local vars
      Scanner sc= new Scanner(System.in);//creating scanner obj
      System.out.println("enter array size:");//promt
      n=sc.nextInt();//no.of ele
        System.out.println("enter no.of ele:");//promt
        a=new int[n];//alocating arr size
        for(int i=0;i<n;i++)
             a[i]=sc.nextInt();
        MergeSort ms=new MergeSort();//creating obj and alocating memory
         ms. mergeSort(a,0,n-1);//invoking mergeSort method
        for(int i=0;i<n;i++)
         System.out.print(a[i]+" ");//result
      }//end of main metthod
};//end of main calss
