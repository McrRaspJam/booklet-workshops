public class CombatProgram
{
	public static void main (String[] args)
	{
		//Create the player
		Character player = new Character();
		player.name = "Wizard";
		player.health = 100;
		player.damage = 25;
		
		//Create the enemy
		Character enemy = new Character();
		enemy.name = "Zombie";
		enemy.health = 75;
		enemy.damage = 25;
		
		//Player attacks enemy
		player.attackCharacter(enemy);
	}
}