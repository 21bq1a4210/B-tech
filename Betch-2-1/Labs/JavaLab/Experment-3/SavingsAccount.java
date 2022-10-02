package SavingsAccout;
/*welcom to SavingsAccount.java
 * In this class contains two instance variable and 3 methods along with a constructor i.e total data members are 5
 */
class SavingsAccount{//start of the class
	/*static varable are beloing to their class not with the object of the class.
	 *they will only inistilized only one when the execution of the code.
	 *single copy will share with all the objects.
	 */
	public static double annual_interest_rate;//static varable syntax: static type var1,var2,var3....
	private double savings_balance;// declaration private instance variable 

	SavingsAccount(double bal){//start of the constructor
	    savings_balance=bal;//inistilising saver balance to instance varable
	}//end of the constructor

	//static method syntax: static type method_name(parameters)
    public static void setInterestRate(double ir){//start of the setInterestRate method
        annual_interest_rate=ir;//inistilising the 
    }//end of the setInterestRate

	public double monthlyInterest(){//start of monthlyInterest method
        double monthly_intrest=(savings_balance*annual_interest_rate)/12;
        savings_balance+=monthly_intrest;
        return savings_balance;
	}//end of monthlyInterest method
	
};//end of the class
