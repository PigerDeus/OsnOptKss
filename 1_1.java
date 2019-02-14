package lab1;
import java.io.File;
import java.io.PrintWriter;
import java.util.Scanner;



public class Lab1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//1.1 Swap a & b
//		int a, b;
//		a = 4;
//		b = 5;
//		a += b;
//		b = a -b;
//		a = a -b;
		//1.2 
		try{
			Scanner scn;
			PrintWriter pw;
			scn = new Scanner(new File("input.txt"));
			pw = new PrintWriter(new File("output.txt"));
			int a = scn.nextInt();
			int b = scn.nextInt();
			a += b;
			b = a -b;
			a = a -b;
			pw.print(a + "   " + b);
			pw.close();
		}
		catch(Exception ex){
			
			
			
			
		}
	}
	
	

}
