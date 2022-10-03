class BubbleSort{
    private static int a[];
    BubbleSort(int[] a){
        this.a=a;
        BubbleSort.sort();
    }
    private static void sort(){
        for(int i=0;i<a.length;i++){
            for(int j=0;j<-i-1;j++){
                if(a[j]>a[j+1]){
                    a[j]+=a[j+1];
                    a[j+1]-=a[j];
                    a[j]+=a[j+1];
                    System.out.printf("iteration:%d res:%d",i,a);
                }
            }
       }
       //System.out.println(a);
    }
}

class Main{
    public static void main(String[] args) {
        int[] a={20,3,17,19,25,35,9,42,16,27};
        BubbleSort bs=new BubbleSort(a);
    }
}