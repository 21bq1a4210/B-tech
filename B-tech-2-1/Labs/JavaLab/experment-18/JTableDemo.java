import javax.swing.JFrame;
import java.awt.FlowLayout;
import javax.swing.*;
public class JTableDemo {
    JFrame f;
    JTable t;
    JTableDemo(){
        f=new JFrame("Student info");
        String data[][]={
            {"21bq1a4210","Sarath","CSM","A"},
            {"21bq1a4209","Eswar","CSM","A"}
        };
        String cols[]={"roll","name","branch","section"};
        t=new JTable(data,cols);
        JScrollPane sp = new JScrollPane(t);
		f.add(sp);
        f.add(t);
        f.setSize(500,500);
        f.setLayout(new FlowLayout());
        f.setVisible(true);
    }
    public static void main(String[] args) {
        new JTableDemo();
    }
}
