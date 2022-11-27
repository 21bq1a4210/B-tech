import javax.swing.JFrame;
import javax.swing.JButton;
public class DemoButtonTest {
    public static void main(String[] args) {
        JFrame frame=new JFrame("welcome");
        JButton button=new JButton("click me");
        frame.add(button);
        frame.setSize(300,300);
        frame.setVisible(true);
    }
}
