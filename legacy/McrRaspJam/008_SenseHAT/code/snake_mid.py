#Libraries
import random
from time import sleep
from copy import deepcopy
#       io
import pygame
from pygame.locals import *
from sense_hat import SenseHat
UH = SenseHat()
hat = SenseHat()

########        Sense Hat Workshop      ##########

difficulty = 0.333 #seconds between turns, lower is harder

def get_input(direction):
	#get accelerometer data
	force = hat.get_accelerometer_raw()
	del force['z']

	if force['x'] < -0.3:
		direction = 3
	elif force['x'] > 0.3:
		direction = 1
	elif force['y'] < -0.3:
		direction = 0
	elif force['y'] > 0.3:
		direction = 2
	
	return direction

##################################################

#extra code
import snakeutils

def draw_game(snake, food, game_over):
	#if the player has lost, don't draw the game
	if game_over:
		for y in range(0,8):
			for x in range(0,8):
				UH.set_pixel(x, y, 50, 0, 0)
	else:
		#clear canvas
		UH.clear()
	
		#draw food (below snake)
		UH.set_pixel(food[0], food[1], 255, 0, 0)
			
		#draw snake
		for i in range(0, len(snake)):
			UH.set_pixel(snake[i][0], snake[i][1], 100, 100, 100)

def main():
	UH.clear()
	
	random.seed()
	pygame.init()
	quit_game = False

	#important game variables
	snake = []
	direction = 0
	food = [0, 0]
	place_food = True
	game_over  = False

	#before entering game loop, set up the start position
	startpos_x = random.randint(0,7)
	startpos_y = random.randint(0,7)
	snake.append([startpos_x, startpos_y])

	#get start position from external code
	direction = snakeutils.startdir(startpos_x, startpos_y)

	#finally, create a pygame window (required for keyboard input)
	pygame.init()
	screen = pygame.display.set_mode((480, 320))
	pygame.display.set_caption('Snake is running')
	pygame.mouse.set_visible(0)
	
	#main game loop
	while quit_game == False:

		direction = get_input(direction)

		#place food if it is not currently placed
		if place_food == True:
			food = snakeutils.place_food(snake)
			place_food = False

		#find the new position of the snake
		head_pos = deepcopy(snake[0])
		head_pos = snakeutils.movement(head_pos, direction)
		
		#the old tail needs to be removed (unless food was just ate)
		if snake[0] == food:
			place_food = True
		else:
			del snake[len(snake)-1]
		
		#shift the list and insert new head
		snake.reverse()
		snake.append(head_pos)
		snake.reverse()


		#finally, check the player hasn't lost:
		#out of bounds
		if (head_pos[0] < 0) or (head_pos[0] > 7):
			game_over = True
		elif (head_pos[1] < 0) or (head_pos[1] > 7):
			game_over = True
		#snake eats its body
		for i in range (1, len(snake)):
			if snake[i] == snake[0]:
				game_over = True

		#draw to output (Unicorn HAT)
		draw_game(snake, food, game_over)
		sleep(difficulty) #change to adjust difficulty

if __name__ == "__main__":
	main()
