import javax.swing.*; 
import java.awt.FlowLayout;
public class TabbedPaneEx { 
 JFrame f; 
 TabbedPaneEx(){ 
 f=new JFrame("JTabbedPane Example"); 
 JPanel p1=new JPanel(); ; 
 JPanel p2=new JPanel(); 
 JPanel p3=new JPanel(); 
 JTabbedPane tp=new JTabbedPane(); 
 //tp.setBounds(50,50,200,200); 
 tp.add("Main",p1); 
 tp.add("Options",p2); 
 tp.add("Help",p3); 
 f.add(tp); 
 f.setSize(400,400); 
 f.setLayout(new FlowLayout()); 
 f.setVisible(true); 
} 
public static void main(String[] args) { 
 new TabbedPaneEx(); 
 } 
}