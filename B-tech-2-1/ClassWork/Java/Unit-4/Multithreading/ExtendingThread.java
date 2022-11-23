class NewThread extends Thread{
    NewThread(){
        super("DemoThread");
        System.out.println("the child thread:"+this);
        start();
    }
    public void run(){
        try{
            for(int i=0;i<6;i++){
                System.out.println(Thread.currentThread().getName()+":"+i);
                Thread.sleep(500);
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
            for(int i=5;i>0;i--){
                System.out.println(Thread.currentThread().getName()+":"+i);
                Thread.sleep(1000);
            }
        }catch(InterruptedException e){
            System.out.println(Thread.currentThread().getName()+"was interrupted");
        }
        System.out.println("end of "+Thread.currentThread().getName());
    }
};