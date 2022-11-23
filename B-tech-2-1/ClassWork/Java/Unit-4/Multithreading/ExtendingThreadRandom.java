import java.util.Random;
class NewThread extends Thread{
    NewThread(){
        super("DemoThread");
        System.out.println("the child thread:"+this);
        start();
    }
    public void run(){
        try{
            Random rand =new Random();
            for(int i=0;i<6;i++){
                int rand_int=rand.nextInt(1000,2500);
                System.out.println(Thread.currentThread().getName()+":"+i+", time:"+rand_int);
                Thread.sleep(rand_int);
            }
        }catch(InterruptedException e){
            System.out.println(Thread.currentThread().getName()+"was interrupted");
        }
        System.out.println("end of "+Thread.currentThread().getName());
    }
};

class ThreadDemo{
    public static void main(String[] args) {
        new NewThread();
        try{
            Random rand =new Random();
            for(int i=0;i<6;i++){
                int rand_int=rand.nextInt(1000,2500);
                System.out.println(Thread.currentThread().getName()+":"+i+", time:"+rand_int);
                Thread.sleep(rand_int);
            }
        }catch(InterruptedException e){
            System.out.println(Thread.currentThread().getName()+"was interrupted");
        }
        System.out.println("end of "+Thread.currentThread().getName());
    }
};