import javax.swing.*;
import javax.swing.tree.DefaultMutableTreeNode;
import java.awt.FlowLayout;
public class JTreeDemo {
    JFrame f;
    JTree t;
    JTreeDemo(){
        f=new JFrame("tree demo");
        DefaultMutableTreeNode style,color,font,red,blue,bold,italic;
        style=new DefaultMutableTreeNode("Style");
        color=new DefaultMutableTreeNode("color");
        font=new DefaultMutableTreeNode("font");
        red=new DefaultMutableTreeNode("red");
        blue=new DefaultMutableTreeNode("blue");
        bold=new DefaultMutableTreeNode("Bold");
        italic=new DefaultMutableTreeNode("italic");
        style.add(color);style.add(font);
        color.add(red);color.add(blue);
        font.add(bold);font.add(italic);
        t=new JTree(style);
        f.add(t);
        f.setSize(400,400);
        f.setVisible(true);
        f.setLayout(new FlowLayout());
    }
    public static void main(String[] args) {
        new JTreeDemo();
    }
}
