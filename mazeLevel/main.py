# Imports the modules used in the game #
import pygame as py
# Although the settings file has other settings for other parts of the game,
# I will only be using some of the settings in this code #
from settings import *

class Game:
	def __init__(self):
		# initialises the game window etc. #
		self.running = True

	def newGame(self):
		# initialises the game (not the game window) #
		pass

	def runLoop(self):
		# The game loop #
		pass

	def update(self):
		# updates the game loop #
		pass

	def events(self):
		# checks for any events that occur #
		pass

	def draw(self):
		# draws onto the screen #
		pass

	def show_start_screen():
		# displays the start screen onto the window #
		pass

	def show_gameOver_screen():
		# displays the game over screen when the user dies or quits the game #
		pass

g = Game()
g.show_start_screen()
while g.running:
	g.new()
	g.show_gameOver_screen()

py.quit()
