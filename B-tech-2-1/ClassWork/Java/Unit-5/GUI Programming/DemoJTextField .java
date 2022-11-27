import javax.swing.JFrame;
import javax.swing.JTextField;

class DemoJTextField  {
    public static void main(String[] args) {
        JFrame frame=new JFrame("Demo TextField");
        JTextField textfield=new JTextField("Type here:");
        frame.setSize(300, 300);
        frame.add(textfield);
        frame.setVisible(true);
    }
}
