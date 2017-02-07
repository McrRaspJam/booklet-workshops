public class PetProgram
{
	public static void main (String[] args)
	{
		//Create a pet
		Pet pet1 = new Pet();
		pet1.name = "Doug"
		pet1.species = "Dog"
		
		//Create a second pet
		Pet pet2 = new Pet();
		pet2.name = "Polly"
		pet2.species = "Parrot"
		
		//print out the pet names
		System.out.println("My two pets are called " + pet1.name + " and " + pet2.name);
	}
}