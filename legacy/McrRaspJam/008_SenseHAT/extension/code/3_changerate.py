from sense_hat import SenseHat
from random import randint
from time import sleep

hat = SenseHat()
snowflakes = []

def main():
	while True:
		add_snowflakes(2)
		draw()
		move()
		sleep(0.2)



def draw():
	hat.clear()

	for snowflake in snowflakes:
		hat.set_pixel(snowflake[0], snowflake[1], 255, 255, 255)



def move():
	for snowflake in snowflakes:
		#move particle down (gravity)
		snowflake[1] += 1

		#move particle randomly about (wind)
		snowflake[0] += randint(-1, 1)

		#delete when off screen
		if snowflake[1] > 7 or snowflake[0] < 0 or snowflake[0] > 7:
			snowflakes.remove(snowflake)



def add_snowflake():
	newflake = [randint(0,7), 0]
	snowflakes.append(newflake)



def add_snowflakes(count):
	count_left = count

	while count_left >= 1:
		add_snowflake()
		count_left -= 1
	
	if count_left > 0:
		count = int(round(1 / count_left, 0))
		if randint(0, count) == 0:
			add_snowflake()




if __name__ == "__main__": main()
