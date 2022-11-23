class Scope{
    static String a="hi hello";
    public static void main(String[] args) {
        int a=100;
        System.out.println(Scope.a);    //hi hello
        System.out.println(a);  //100
    }
};