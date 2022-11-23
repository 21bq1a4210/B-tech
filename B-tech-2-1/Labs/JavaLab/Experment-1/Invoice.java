package Invoice;
/* 
Welcome to Invoice.java
In this sourse code they are 10 methods along with constructor and 4 instance variable. i.e total data members are 14.
*/
class Invoice{
	// declaration private instance variable of different data type
	private String number,description;
	private int quantity;
	private double prise;
	//Zero paratemersed constructure.
	Invoice(){ //starting of constructor method
	    //instance variable are initialize to NULL(empty or zero)
		number="";
		description="";
		quantity=0;
		prise=0.0;
	}//ending of constructor method
	
	public void setNumber(String num){//starting of setNumber method
		number=num; //stores the item number of Sting type 
	}//ending of setNumber method
	
	public String getNumber(){//starting of getNumber method
		return number; //returns the number of String type
	}//ending of getNumber method
	
	public void setDescription (String des){//starting of setDescription method
		description=des; //stores the description of item of String type
	}//ending of setDescription
	public String getDescription (){//starting of getDescription method
		return description;//returns the description of String type
	}//ending of setDescription method

	public void setQuantity(int qua){//statiing of setQuantity method
		quantity=qua;//stores the quantity of item of int type
	}//enging of setQuantity method
	public int getQuantity(){//stating of getQuantity method
		return quantity;//returns the quantity of int type
	}//ending of getQuantity method

	public void setPrise(double pri){//starting of setPrise method
		prise=pri;//stores the prise of item of double type
	}//ending of setPrise method
	public double getPrise(){//sarting of getPrise method
		return prise;//returns the prise 
	}//ending of getPrise method
	
	public double  getInvoiceAmount(){//starting of getInvoiceAmount method
		if (quantity<0) quantity=0; //checking quantity if it is negative setting it to zero
		if (prise<0) prise=0.0; //checking prise if it is negative setting it to 0.0
		return quantity*prise; //finally returning the total prise
	}//ending of getInvoiceAmount method
};//end of Invoice class
