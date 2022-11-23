import java.math.pow;
public class Ex2_calc_ligthyear {
    public static void main(String[] args) {    //s=d/t
        double distance;
        double speed_ligth=3*Math.pow(10, 8);
        //System.out.println(speed_ligth);
        double time= 365.25*24*60*60;  //total time
        //System.out.println(time);
        distance = speed_ligth*time;    //distance
        System.out.println("a ligth year="+distance+"m");
    }
}