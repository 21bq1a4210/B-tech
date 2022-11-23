import java.util.Random; 
class NewThread implements Runnable{
    Thread t;
    NewThread(){
        t=new Thread(this,"Demo thread");
        System.out.println("the demo thread:"+t);
        t.start();
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

//output
//test-case-1:
/*the demo thread:Thread[Demo thread,5,main]
main:0, time:1783
Demo thread:0, time:2178
main:1, time:1330
Demo thread:1, time:1607
main:2, time:1190
Demo thread:2, time:1232
main:3, time:2284
Demo thread:3, time:1864
main:4, time:1329
Demo thread:4, time:1263
main:5, time:1461
Demo thread:5, time:2397
end of main
end of Demo thread */

//test case-2:
/*the demo thread:Thread[Demo thread,5,main]
Demo thread:0, time:1403
main:0, time:1679
Demo thread:1, time:2348
main:1, time:2058
main:2, time:2286
Demo thread:2, time:2038
Demo thread:3, time:2374
main:3, time:1084
main:4, time:2290
Demo thread:4, time:1772
main:5, time:1217
Demo thread:5, time:2119
end of main
end of Demo thread */