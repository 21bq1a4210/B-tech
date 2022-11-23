class BubbleSort{
    private static int a[];
    BubbleSort(int a[]){
        this.a=new int[a.length];
        for(int i=0;i<a.length;i++){
            this.a[i]=a[i];
        }
        BubbleSort.sort();
    }
    private static void sort(){
        for(int i=0;i<a.length;i++){
            for(int j=0;j<a.length-i-1;j++){
                if(a[j]>a[j+1]){
                    int temp=a[j];
                    a[j]=a[j+1];
                    a[j+1]=temp;
                }
            }
        }
        System.out.print("sorted array:");
        for(int i=0;i<a.length;i++){
            System.out.print(a[i]+" ");
        }

    }
}

class Main{
    public static void main(String[] args) {
        int []a={9,23,21,11,43,33};
        BubbleSort bs=new BubbleSort(a); 
    }
};