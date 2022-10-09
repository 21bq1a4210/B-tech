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

            if(rand_int1==rand_int2){//start of if block
                arr[--rand_int1]+=1;//if both are equal then increasing the arr[rand_int1-1] cuz index start from 0
            }//end of if block
        }//end of for block
    }//end of random method
   
    private void display(){//start of display method
        for(int i=0;i<arr.length;i++){//start of for block
            System.out.println("("+(i+1)+","+(i+1)+")"+"="+arr[i]);
        }//end of for block
    }//end of display method 
}//end of PairDies class

class Main{//start Main class
    public static void main(String args[]) { //start of main method
        PairDies pd=new PairDies();////creating an obj of PairDies class and allocating memory 
	} //end of main method
}; //end of main class
