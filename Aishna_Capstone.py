# SPGL Minimal Code by /u/wynand1004 AKA @TokyoEdTech
# Requires SPGL Version 0.8 or Above
# SPGL Documentation on Github: https://wynand1004.github.io/SPGL
# Use this as the starting point for your own games

# Import SPGL
import spgl
import random
import turtle

# Create Classes

class Game(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)
		self.shape("ground.gif")
		
class Player(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)
		self.frame = 0
		self.y_acceleration = 5
		self.y_speed = 5
		self.strength = 7
		self.score = 0
		self.state = "running"
		self.lives = 3
		
	def score(self):
		self.score = 0			
	
	def lives(self):
		self.lives = 3
	
	def up(self):
		if self.state == "running":
			self.shape("mario.gif")
			self.y_acceleration += self.strength
			self.sety(0)
			self.state = "jumping"
	
	def down(self):
		self.set_image("Mario_Crouch.gif", 150, 145)
		self.sety(-90)
		self.state = "crouching"
	
	def tick(self):
		self.setx(self.xcor())
		
		if self.ycor() < -80:
			self.y_acceleration = 1
			self.y_speed = 1
			self.sety(-90)
			self.state = "running"
			
		self.y_acceleration += game.gravity
		self.y_speed += self.y_acceleration
		self.sety(self.ycor() + self.y_speed)

class Plant(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)	
		self.frame = 0
		self.speed = -10
		self.shape("plant.gif")

	def tick(self):
		self.fd(self.speed)

class Shell(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)	
		self.frame = 0
		self.speed = -10
	def tick(self):
		self.fd(self.speed)

class Coin(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)


# Create Functions

# Initial Game setup
game = spgl.Game(800, 600, "black", "Aishna Capstone Project", 0)
game.gravity = -1

# Create Sprites
player = Player("mario.gif", "blue", -200, -100)
shell = Shell("shell.gif", "red",random.randint(100,1000), -6)
plant = Plant("plant.gif", "white", random.randint(100,1000), -100)
ground = Game("ground.gif", "blue", 0, -110)


# Create Label
label_name = spgl.Label("MARIO RUN", "white", 50, 100)  
label_name.set_font_name("SuperMarioBrosWii")
label_name.set_font_size(50)
score_label = spgl.Label("Score: 0", "white", -380, 280)
lives_label = spgl.Label("Lives: 3", "white", -280, 280)


# Set Keyboard Bindings
game.set_keyboard_binding(spgl.KEY_UP, player.up)
game.set_keyboard_binding(spgl.KEY_DOWN, player.down)

while True:
    # Call the game tick method
	game.tick()
	if game.is_collision(player, plant):
		player.lives += -1
		lives_label.update("Lives: {}".format(player.lives))
		plant.goto(random.randint(300,600), -100)
		
		
	if game.is_collision(player, shell):
		player.lives += -1
		lives_label.update("Lives: {}".format(player.lives))
		shell.goto(random.randint(600,900), -20)

	if player.xcor() == plant.xcor() and player.xcor() == shell.xcor():
		player.score += 1
		
	if plant.xcor() < -500:
		plant.goto(random.randint(300,600), -100)
		
	if shell.xcor() < -500:
		shell.goto(random.randint(600,900), -20)

# 	if player.lives > -1:
# 		label_name = spgl.Label("GAME OVER", "white", -200, 100)  
# 		label_name.set_font_name("SuperMarioBrosWii")
# 		label_name.set_font_size(50)		