package SavingsAccout;
//welcom to SavingsAccountTest.java
class SavingsAccountTest{//start of the class
    public static void main(String args[]){//main method begins execution of Java application
        // create a SavingsAccount object and assign it to saver1
        SavingsAccount saver1=new SavingsAccount(2000.00);

        // create a SavingsAccount object and assign it to saver2
        SavingsAccount saver2=new SavingsAccount(3000.00);

        SavingsAccount.setInterestRate(0.04);//set the interst rate
        //display initial data of the new balance of both the users when intrest rate is 4%
        System.out.println("new balance for saver1 when interest rate is 4%:"+ String.format("%.2f", saver1.monthlyInterest()));
        System.out.println("new balance for saver2 when interest rate is 4%:"+String.format("%.2f", saver2.monthlyInterest()));

        SavingsAccount.setInterestRate(0.05);//set the interst rate
        //display initial data of the new balance of both the users when intrest rate is 5%
        System.out.println("new balance for saver1 when interest rate is 5%:"+String.format("%.2f", saver1.monthlyInterest()));
        System.out.println("new balance for saver2 when interest rate is 5%:"+String.format("%.2f", saver2.monthlyInterest()));

    }//end of main method

};//end of the class
