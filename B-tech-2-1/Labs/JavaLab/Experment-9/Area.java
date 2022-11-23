/*Write a Java Program to create an abstract class named Shape that contains two integers and 
an empty method named print Area(). Provide three classes named Rectangle, Triangle and 
Circle such that each one of the classes extends the class Shape. Each one of the classes 
contains only the method print Area () that prints the area of the given shape.[CO2]*/

abstract class Shape{ //abstract class 
    public int length,breadth;
    abstract public void Area();    //incomplet methode 
};

class Rectangle extends Shape{  //to calc area of Rectangle shape  
    Rectangle(int length,int breadth){
        super.length=length;
        super.breadth=breadth;
    }
    @Override
    public void Area(){
        System.out.println("the area of the Rectangle:"+(super.length*super.breadth));
    }
};

class Triangle extends Shape{   //to calc area of Triangle shape  
    Triangle(int heigth,int base){
        super.length=heigth;
        super.breadth=base;
    }
    @Override
    public void Area(){
        System.out.println("the area of the Triangle:"+(0.5*super.length*super.breadth));
    }
};

class Circle extends Shape{ //to calc area of Circle shape  
    Circle(int radius){
        super.length=radius;
    }
    @Override
    public void Area(){
        System.out.println("the area of the Circle:"+(3.14*super.length*super.length));
    }
};

class Main{
    public static void main(String[] args) {
        Shape rect=new Rectangle(10, 10);
        rect.Area();
        Shape tri=new Triangle(10, 10);
        tri.Area();
        Shape cir=new Circle(10);
        cir.Area();
    }
};