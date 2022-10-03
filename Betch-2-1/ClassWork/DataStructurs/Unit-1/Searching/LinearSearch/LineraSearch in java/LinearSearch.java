class LinearSearch{
    private static int[] a;
    private static int key;
    LinearSearch(int a[],int key){
        this.a=new int[a.length];
        for(int i=0;i<a.length;i++){
            this.a[i]=a[i];
        }
        this.key=key;
        LinearSearch.search();
    }
    private static void search(){
        int f=0,i;
        for(i=0;i<a.length;i++){
            if(key==a[i]){
                f++;
                break;
            }
        }
        if(f!=0) System.out.println("element found at location:"+(i+1));
        else System.out.println("element not found");
    }
    
}

class Main {
    public static void main(String[] args) {
        int a[]={10,20,40,50};
        LinearSearch ls1=new LinearSearch(a, 50);
        LinearSearch ls2=new LinearSearch(a, 03);
    }
}
