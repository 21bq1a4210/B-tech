public class LinearSearch {
    public static void main(String[] args) {
        int a[]={10,20,40,50};
        int key=50,f=0,i;
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
