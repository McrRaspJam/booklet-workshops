public class Character
{
	public String name;
	public int health;
	public int damage;	//attack damage
	
	public void attackCharacter(Character opponent)
	{
		opponent.health -= this.damage;
		
		System.out.println(this.name + " attacked " + opponent.name + " for " + this.damage + "HP");
	}
}