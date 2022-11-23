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
//test-case-1:
/*the demo thread:Thread[Demo thread,5,main]
Demo thread:0
main:5
Demo thread:1
main:4
Demo thread:2
Demo thread:3
main:3
Demo thread:4
Demo thread:5
main:2
end of Demo thread
main:1
end of main */

//test case-2:
/*the demo thread:Thread[Demo thread,5,main]
main:5
Demo thread:0
Demo thread:1
main:4
Demo thread:2
Demo thread:3
main:3
Demo thread:4
Demo thread:5
main:2
end of Demo thread
main:1
end of main */

//test case-3:
/*the demo thread:Thread[Demo thread,5,main]
main:5
Demo thread:0
Demo thread:1
Demo thread:2
main:4
Demo thread:3
Demo thread:4
main:3
Demo thread:5
main:2
end of Demo thread
main:1
end of main */