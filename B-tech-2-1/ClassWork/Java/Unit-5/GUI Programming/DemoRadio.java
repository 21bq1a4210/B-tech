import javax.swing.JFrame;
import java.awt.FlowLayout;
import javax.swing.JTextField;
import javax.swing.JRadioButton;
import javax.swing.ButtonGroup;
import java.awt.Font;
import java.awt.event.ItemListener;
import java.awt.event.ItemEvent;
class RBDemo{
    static JTextField text;
    public static void main(String[] args) {
        JFrame frame = new JFrame("RadioButton Demo");
        frame.setLayout( new FlowLayout() );

        text=new JTextField( "Watch the font style change", 25);
        frame.add(text);

        //Create the radio buttons.
        JRadioButton plainrb = new JRadioButton("plain",true);
        JRadioButton boldrb = new JRadioButton("bold",false);
        JRadioButton italicrb = new JRadioButton("italic",false);
        JRadioButton BIrb = new JRadioButton("bolditalic",false);

        // create logical relationship between JRadioButtons
        ButtonGroup bg=new ButtonGroup();    // create ButtonGroup
        bg.add(plainrb); bg.add(boldrb); bg.add(italicrb); bg.add(BIrb);

        frame.add(plainrb); frame.add(boldrb); frame.add(italicrb); frame.add(BIrb);

        frame.setVisible(true);
        frame.setSize(300,150);

        // create font objects
        Font plainFont = new Font( "Serif", Font.PLAIN, 14 );
        Font boldFont = new Font( "Serif", Font.BOLD, 14 );
        Font italicFont = new Font( "Serif", Font.ITALIC, 14 );
        Font boldItalicFont = new Font( "Serif", Font.BOLD + Font.ITALIC, 14 );
        text.setFont( plainFont ); // set initial font to plain

        plainrb.addItemListener(new RadioButtonHandler( plainFont ) );
        boldrb.addItemListener(new RadioButtonHandler( boldFont ) );
        italicrb.addItemListener(new RadioButtonHandler( italicFont ) );
        BIrb.addItemListener(new RadioButtonHandler( boldItalicFont ) ); 
    }
}
class RadioButtonHandler extends RBDemo implements ItemListener{
    Font f;
    RadioButtonHandler(Font f){
        this.f=f;
    }
    public void itemStateChanged( ItemEvent event ){
        text.setFont( f );
    }
}