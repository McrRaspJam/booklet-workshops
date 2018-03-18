import java.lang.*;

public class Vector3
{
	public double x;
	public double y;
	public double z;
	
	public double magnitude()
	{
		// Magnitude is the 
		// square root of x^2 + y^2 + z^2
		double sum = Math.pow(x, 2) + Math.pow(y, 2) + Math.pow(z, 2);
		
		return Math.sqrt(sum);
	}
}