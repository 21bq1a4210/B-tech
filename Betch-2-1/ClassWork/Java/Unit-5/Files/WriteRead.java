import java.io.*;

class WriteRead 
{
	public static void main(String[] args) 
		throws IOException
	{
	   FileWriter out = 
		   new FileWriter("sample.txt");

	   char ch = 'a';
	   char chars[]={'b','c','d','e','f'};

	   out.write( ch );
	   out.write( chars );

	   out.close();

	   FileReader in = new FileReader("sample.txt");

	   char ch1 = (char)in.read();
	   char buffer[] = new char[10];
	   
	   in.read(buffer);

	   System.out.println( ch1 );
	   System.out.println( buffer );

	   in.close();
	}
}
