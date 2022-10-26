class NewThread implements Runnable{
    Thread t;
    NewThread(){
        t=new Thread(this,"Demo thread");
        System.out.println("the demo thread:"+t);
        t.start();
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
        NewThread nt=new NewThread();
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