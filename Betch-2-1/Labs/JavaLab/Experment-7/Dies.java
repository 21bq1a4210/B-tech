import java.util.Random; 

class generateRandom{ 

	public static void main(String args[]) 
	{ 
        int arr[]=new int[6];
		Random rand = new Random(); 
        for(int i=0;i<1000;i++){
            int rand_int1 = rand.nextInt(1,7); 
		    int rand_int2 = rand.nextInt(1,7);
            if(rand_int1==rand_int2){
                int j=rand_int1;
                j--;
                arr[j]+=1;
            }
		    /*System.out.println("Random Integers: "+rand_int1); 
		    System.out.println("Random Integers: "+rand_int2);
            */
        } 
        for(int i=0;i<arr.length;i++){
            System.out.println(arr[i]+" ");
        }
	} 
} 
