import java.lang.*;

public class Vector3
{
	public float x;
	public float y;
	public float z;
	
	public float magnitude()
	{
		// Magnitude is the 
		// square root of x^2 + y^2 + z^2
		float sum = Math.pow(x, 2) + Math.pow(y, 2) + Math.pow(z, 2);
		
		return Math.sqrt(sum);
	}
	
	public Vector3(float xIn, float yIn, float zIn)
	{
		x = xIn;
		y = yIn;
		z = zIn;
	}
}