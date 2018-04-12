# SPGL Minimal Code by /u/wynand1004 AKA @TokyoEdTech
# Requires SPGL Version 0.8 or Above
# SPGL Documentation on Github: https://wynand1004.github.io/SPGL
# Use this as the starting point for your own games

# Import SPGL
import spgl
import random
# Create Classes


class Player(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)
		self.frame = 0
		self.y_acceleration = 5
		self.y_speed = 5
		self.strength = 7
		self.score = 3
		self.state = "running"
		
# sprite_name.set_bounding_box(width, height)

	def score(self):
		self.score = 3
	
# 	def right(self):
# 		self.setx(self.xcor() + 10)
		
	def up(self):
		if self.state == "running":
			self.y_acceleration += self.strength
			self.sety(0)
			self.state = "jumping"
	
	def tick(self):
		self.setx(self.xcor())
		if self.ycor() < -90:
			self.y_acceleration = 1
			self.y_speed = 1
			self.sety(-100)
			self.state = "running"
			
		self.y_acceleration += game.gravity
		self.y_speed += self.y_acceleration
		self.sety(self.ycor() + self.y_speed)

class Plant(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)	
		self.frame = 0
		self.speed = -6

	def tick(self):
		self.fd(self.speed)

# 	def ressurect(self):

# sprite_name.set_bounding_box(width, height)

		
class Bird(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)	
		self.frame = 0
		self.speed = -6
	def tick(self):
		self.fd(self.speed)

# Create Functions

# Initial Game setup
game = spgl.Game(800, 600, "black", "Aishna Capstone Project", 0)
game.gravity = -1

# Create Sprites
bird = Bird("triangle", "red",random.randint(0,1000), -90)
bird = Bird("triangle", "red",random.randint(0,1000), -90)
player = Player("circle", "blue", -200, -100)

plant = Plant("square", "white", random.randint(0,1000), -100)


# Create Label
label_name = spgl.Label("MARIO RUN", "white", 50, 100)  
label_name.set_font_name("SuperMarioBrosWii")
label_name.set_font_size(50)
score_label = spgl.Label("Score: 0", "white", -380, 280)


# Set Keyboard Bindings
game.set_keyboard_binding(spgl.KEY_UP, player.up)
# game.set_keyboard_binding(spgl.KEY_DOWN, player.down)

while True:
    # Call the game tick method
	game.tick()
	if game.is_collision(player, plant):
		player.score += -1
		score_label.update("Score: {}".format(player.score))
		
	if game.is_collision(player, bird):
		player.score += -1
		score_label.update("Score: {}".format(player.score))
		
	if plant.xcor() < -500 or plant.xcor():
		Plant("square", "white", random.randint(0,1000), -100)
