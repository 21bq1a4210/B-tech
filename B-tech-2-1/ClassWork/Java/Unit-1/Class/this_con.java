class A{  
    
    A(){
        this(5);
        System.out.println("hello a");
    }  
    A(int x){  
        //this();  
        System.out.println(x);  
    }
};

class TestThis5{  
    public static void main(String args[]){  
        A a=new A(10);  
    }
};  