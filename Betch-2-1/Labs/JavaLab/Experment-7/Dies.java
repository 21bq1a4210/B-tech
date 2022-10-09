import java.util.Random; //importing Random class
class PairDies{//start of PairDies class
    int arr[]=new int[6];//creating and alocating memory for arr which used to store the result
    PairDies(){//start of constructor
        random();//invoking the random method of PairDies class
        display();//invoking the display method of PairDies class
    }//end of constructor

    private void random(){//start of private random method (rolling a pair of dies)
		Random rand = new Random(); //creating an obj of Random class and allocating memory 
        for(int i=0;i<10_000;i++){//start of for loop iterating over 10k time by the pb
            int rand_int1 = rand.nextInt(1,7);//storing a random in in b/w 1 to 6 in rand_int1
		    int rand_int2 = rand.nextInt(1,7);//storing a random in in b/w 1 to 6 in rand_int2
            if(rand_int1==rand_int2){//if both are equal then increasing the arr[index-1]
                int j=rand_int1;
                j--;
                arr[--rand_int1]+=1;
            }
        }
    }
   
    private void display(){
        for(int i=0;i<arr.length;i++){
            System.out.println("("+(i+1)+","+(i+1)+")"+"="+arr[i]);
        }
    }
        
}
class Main{ 
    public static void main(String args[]) { 
        PairDies pd=new PairDies();
	} 
} 
