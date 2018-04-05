# SPGL Minimal Code by /u/wynand1004 AKA @TokyoEdTech
# Requires SPGL Version 0.8 or Above
# SPGL Documentation on Github: https://wynand1004.github.io/SPGL
# Use this as the starting point for your own games

# Import SPGL
import spgl

# Create Classes
class Player(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)
		self.frame = 0
		
	def move(self):
		self.fd(self.speed)
		
	def increasespeed(self):
		self.speed += 1
		if self.speed >10:
			self.speed = 10		
		
	def tick(self):
		self.frame += 1
		if self.frame % 10 == 0:
			self.color("red")
		elif self.frame % 15 == 0:
			self.color("blue")
			self.frame = 0
			
	def right(self):
		self.setx(self.xcor() + 10)
		
	def jump(self):
		self.y_acceleration += self.strength
		self.sety(1)
	
	def tick(self):
		self.setx(self.xcor() + 3)
		
		if self.ycor() < 0:
			self.y_acceleration = 0
			self.y_speed = 0
			self.sety(0)
			
		self.y_acceleration += game.gravity
		self.y_speed += self.y_acceleration
		self.sety(self.ycor() + self.y_speed)

class Plant(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)	
		self.frame = 0

	def move(self):
		self.fd(self.speed)


		
# Create Functions

# game.gravity = -2

# Initial Game setup
game = spgl.Game(800, 600, "black", "Aishna Capstone Project", 0)

# Create Sprites
player = Player("circle", "blue", 100, -100)
plant = Plant("square", "white", 100, -100)

# Create Labels

# Create Buttons

# Set Keyboard Bindings
game.set_keyboard_binding(spgl.KEY_RIGHT, player.right)
game.set_keyboard_binding(spgl.KEY_LEFT, player.left)

while True:
    # Call the game tick method
    game.tick()
