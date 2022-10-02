package Book;
/*welcom to Book.java
 * In this class contains 4 instance variable and 10 methods along with a constructor i.e total data members are 14
 */
class Book{//start of the class
    //declaration private instance variable of different types
    private String name;
    private int ISBN;
    private String author;
    private String publisher;

    Book(){//start of constructor
        this.name="";
        this.ISBN=0;
        this.author="";
        this.publisher="";
    }//end of constructor

    /*Mutator Methods:
     * In Java, mutator methods reset the value of a private variable.
     * This gives other classes the ability to modify the value stored in that variable without having direct access to the variable itself.
     * In Java, mutator methods reset the value of a private variable.
     * This gives other classes the ability to modify the value stored in that variable without having direct access to the variable itself.
     * In this class Book the mutator method are setName,setISBN,setAuthor and setPublisher.
     */
    public void setName(String name){//start of setName method
        /*this can be used inside any method to refer to the current object.
         *this is always a reference to the object on which the method was invoked.
         *here the parameter is same as intance varable. in this case jvm will confuse.
         when we use this keyword that refers to method
         */
        this.name=name;//stores the name of book of Sting type 
    }

    public void setISBN(int ISBN){//start of setISBN
        this.ISBN=ISBN;//stores the ISBN of book of int type
    }//end of setISBN

    public void setAuthor(String author){//start of setAuthor method
        this.author=author;//store the author name of the book of type string
    }//end of setAuthor

    public void setPublisher(String publisher){//start of setPublisher method
        this.publisher=publisher;//store the publisher of the book of type string
    }//end of setPublisher method

    /*Accessor Methods:
     * In Java, accessor methods return the value of a private variable.
     * This gives other classes access to that value stored in that variable. 
     * Without having direct access to the variable itself.
     * Accessor methods take no parameters and have a return type that matches the type of the variable they are accessing.
     */
    public String getName(){//start of getName method
        return this.name;//returns the name of the book of string type
    }//end of the method

    public int getISBN(){//start of getISBN method
        return this.ISBN;//return the ISBN of the book of int type
    }//end of getISBN method

    public String getAuthor(){//start of getAuthor method
        return this.author;//return the author name of the book of string type
    }//end of getAuthor method

    public String getPublisher(){//start of getPublisher method
        return this.publisher;//return the publisher of the book of string type
    }//end of the getPublisher method

    //dsiplying the book description
    public void getBookInfo(){//start of the grtBookInfo
        System.out.println("Name of book:"+getName());//display initial data of the book's name
        System.out.println("Name of ISBN:"+getISBN());//display initial data of the book's ISBN
        System.out.println("Name of author:"+getAuthor());//display initial data of the book's author
        System.out.println("Name of publisher:"+getPublisher());//display initial data of book's publisher
    }//end of the grtBookInfo
};//end of the Book class
