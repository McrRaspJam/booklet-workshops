public class Pet
{
	public String name;
	public String species;
	
	private int treats;
	
	public void giveTreat()
	{		
		Random rand = new Random();
		boolean eatnow = rand.nextBoolean();
		
		//Store treat if not ate.
		if (eatnow == false)
			treats = treats + 1;
	}
	
	public int getNumberOfTreats()
	{
		return treats;
	}
}