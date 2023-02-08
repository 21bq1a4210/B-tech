class WatingState {
    public void createWatingThread(){
        Thread t1 = new Thread(new Task1());
        t1.start();
        System.exit(0);
    }
}
class Task1 implements Runnable {
    @Override
    public void run(){
        Thread t2=new Thread(new Task2());
        try{
            t2.start();
            t2.join();
        }catch(InterruptedException e){
            System.out.println(e);
        }
        //put t1 in wating state untill t2 finish 
    }
}
class Task2 extends WatingState implements Runnable{
    @Override
    public void run(){
        try{
            Thread.sleep(2000);
            //WATING
            System.out.println("Thread State:"+t1.getState());
        }catch(InterruptedException e){
            System.out.println(e);
        }
    }
};
