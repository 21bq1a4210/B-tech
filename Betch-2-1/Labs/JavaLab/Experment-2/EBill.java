package EBill;
/*
*welcom to EBill.java
*In this class they are only 3 methods along with constructor and 3 private and 2 public instance varables 
*/
public class EBill{//start of the EBill class
	//declaration public and private instance variable of different data type
	public String consumer_no,consumer_name;
	private double previous_month_reading,current_month_reading,units;
	/*paramaterised constructor
	with takes num,name,pr,cr as a parameters and private instance variable are initialization take place*/
	EBill(String num, String name, double pr,double cr){//start of constructor method
		consumer_no=num;
		consumer_name=name;
		previous_month_reading=pr;
		current_month_reading=cr;
	}//end of constructor method
	
	public double domestic(){//start of domestic method
	    units=current_month_reading - previous_month_reading;
	    if (units<=100) return units*1; //fee for 1st 100 units
	    else if(units<=200) return 100+(units-100)*2.5; //fee for 1st 100 units + 101-200 inits 
	    else if(units<=500) return 100+(units-100)*2.5+(units-300)*4;//fee for 1st 100 units + 101-200 units + 201-500 units
	    else return 100+(units-100)*2.5+(units-300)*4+(units-500)*6;//fee for 1st 100 units + 101-200 units + 201-500 units + >501 unis
	}//end of domestic method
	public double commercial(){//start of commercial method
	    units=current_month_reading - previous_month_reading;
	    if (units<=100) return units*2;//fee for 1st 100 units
	    else if(units<=200) return 100+(units-100)*4.5;//fee for 1st 100 units + 101-200 inits 
	    else if(units<=500) return 100+(units-100)*4.5+(units-300)*6;//fee for 1st 100 units + 101-200 units + 201-500 units
	    else return 100+(units-100)*4.5+(units-300)*6+(units-500)*7;//fee for 1st 100 units + 101-200 units + 201-500 units + >501 unis
	}//end of commercial method
};//end of EBill class
