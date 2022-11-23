class NewThread implements Runnable{
    Thread t;
    NewThread(String s){
        t=new Thread(this,s);
        System.out.println("thread name:"+t);
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
        new NewThread("T1");
        new NewThread("T2");
        new NewThread("T3");
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
