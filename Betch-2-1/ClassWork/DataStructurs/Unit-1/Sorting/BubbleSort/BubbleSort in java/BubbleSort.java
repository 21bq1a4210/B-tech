class Demo{
    public static void main(String[] args) {
        int []a={9,23,21,11,43,33};
        for(int i=0;i<a.length;i++){
            for(int j=0;j<a.length-i-1;j++){
                if(a[j]>a[j+1]){
                    int temp=a[j];
                    a[j]=a[j+1];
                    a[j+1]=temp;
                    System.out.print("iteration:"+(i+1)+" ");
                }
            }
        }

        for(int i=0;i<a.length;i++){
            System.out.print(a[i]+" ");
        }
    }
};