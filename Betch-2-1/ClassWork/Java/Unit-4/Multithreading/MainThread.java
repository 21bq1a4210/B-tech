class MainThread extends Thread{
    public static void main(String[] args) {
        Thread t = Thread.currentThread();
        /*t.setName("my thread");
        t.setPriority(MIN_PRIORITY);
        System.out.println(t.getName()+" "+t.getId()+" "+t.getState()+" "+t.getPriority());
        */
        System.out.println("current thread:"+t);
        t.setName("my thread");
        System.out.println("after changeing name"+t);

        try{
            for(int i=10;i>0;i--){
                System.out.println(i);
                Thread.sleep(1000);
            }
        }catch(InterruptedException e){
            System.out.println("this is an error");
        }
    }
};
