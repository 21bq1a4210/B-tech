import java.lang.Thread;
import java.lang.System;
import java.lang.Exception;
import java.util.Random;
class Rand implements Runnable{
    Thread t;
    static int rand; 
    Rand(){
        t=new Thread(t,"Rand");
        t.start();
    }
    public void run(){
        Random r=new Random();
        rand=r.nextInt(0,100);
        
    }
}