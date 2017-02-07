public class PetProgram
{
	public static void main (String[] args)
	{
		//Create a pet
		Pet pet1 = new Pet();
		pet1.name = "Doug"
		pet1.species = "Dog"
		
		//feed the pet some treats
		pet1.giveTreat();
		pet1.giveTreat();
		pet1.giveTreat();
		
		//how many treats did the pet store?
		System.out.println(pet1.name + " has " + pet1.getNumberOfTreats() + " treats.");
	}
}