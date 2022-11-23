class ShiftOpp{
    public static void main(String[] args) {
        int a = -16;
        System.out.println(a>>2);//-4
        System.out.println(a>>>2);//1073741820
        int b = 16;
        System.out.println(b>>2);//4
        System.out.println(b>>>2);//4
    }
};