from sense_hat import SenseHat
from random import randint
from time import sleep

hat = SenseHat()
snowflakes = []

def main():
	while True:
		add_snowflake()
		draw()

		sleep(0.2)



def draw():
	hat.clear()

	for snowflake in snowflakes:
		hat.set_pixel(snowflake[0], snowflake[1], 255, 255, 255)



def move():
	pass


def add_snowflake():
	newflake = [randint(0,7), 0]
	snowflakes.append(newflake)



if __name__ == "__main__": main()
