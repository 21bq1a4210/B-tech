import java.util.jar.Manifest;

abstract class Shape {  //super class or abstract class
    abstract public void display(); //a method of incomplet behivour
};

abstract class D2 extends Shape{    //child class or concreat class of Shape
    double length,depth;     //local varables
    abstract public double area();  //a method of incomplet behivour
};

abstract class D3 extends Shape{    //child class or concreat class of Shape
    double length,depth,hight;   //local varables
    abstract public double volume();    //a method of incomplet behivour
};

class Circle extends D2{    //child class of concreat class (D2)
    Circle(double radius){
        length=radius;
    }
    @Override
    public double area(){   //redefined for behivour 
        return (22/7)*length*length;
    }
    @Override
    public void display(){
        System.out.println("the area of the circle:"+area()+"sqrt U");
    }
};

class Cube extends D3{      //child class of concreat class (D2
    Cube(double side){
        length=side;
    }
    @Override
    public double volume(){   //redefined for behivour
        return length*length*length;
    }
    @Override
    public void display(){
        System.out.println("the area of the square:"+volume()+"sqrt U");
    }
};

class Main{
    public static void main(String[] args) {
        Shape s1= new Circle(10);
        s1.display();

        Shape s2 = new Cube(10);
        s2.display();
    }
}