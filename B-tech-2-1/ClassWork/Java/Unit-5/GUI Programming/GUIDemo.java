import javax.swing.*;
class GUIDemo {
    public static void main(String[] args) {
        GUIDemo gui=new GUIDemo();
        gui.go();
    }
    void go{
        JFrame frame=new JFrame("welcome");
        JButton button=new JButton("click me");
        button.addActionListener(this);
        frame.add(button);
        frame.setSize(300,300);
        frame.setVisible(true);
    }
    public void actionPerforer(ActionEvent AE){
        button.setText("i have been clicked");
    }
}
