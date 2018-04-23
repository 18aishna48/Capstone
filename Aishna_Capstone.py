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
		self.lives = 6
		
	def score(self):
		self.score = 0			
	
	def lives(self):
		self.lives = 6
	
	def up(self):
		if self.state == "running":
			self.shape("mario_run.gif")
			self.y_acceleration += self.strength
			self.sety(0)
			self.state = "jumping"
	
	def down(self):
		self.set_image("Mario_Crouch.gif", 150, 145)
		self.state = "crouching"
		self.sety(-105)
				
	def tick(self):
		self.setx(self.xcor())
		
		if self.ycor() < -80:
			self.y_acceleration = 1
			self.y_speed = 1
			self.sety(-95)
			self.state = "running"
			
			if self.state == "crouching":
				self.sety(-200)
			
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
		self.frame = 0
		self.speed = -10
		self.shape("coin.gif")

	def tick(self):
		self.fd(self.speed)

class Banana(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)	
		self.frame = 0
		self.speed = -10
		self.shape("banana.gif")

	def tick(self):
		self.fd(self.speed)

# Create Functions

# Initial Game setup
game = spgl.Game(800, 600, "black", "Aishna Capstone Project", 0)
game.gravity = -1

# Create Sprites
ground = Game("ground.gif", "blue", 0, -110)
player = Player("mario_run.gif", "blue", -200, -100)
player.set_image("mario_run.gif", 90, 116)
shell = Shell("shell.gif", "red",random.randint(105,1000), -6)
shell.set_image("shell.gif",106, 113)
plant = Plant("plant.gif", "white", random.randint(95,1000), -100)
coin = Coin("coin.gif", "white", random.randint(100,1000), -6)
banana = Banana("banana.gif", "black", random.randint(100,1000), -130)

objects = [shell, plant, coin, banana]

# Create Label
label_name = spgl.Label("MARIO RUN", "white", -70, 150)  
label_name.set_font_name("SuperMarioBrosWii")
label_name.set_font_size(50)
score_label = spgl.Label("Score: 0", "white", -380, 280)
lives_label = spgl.Label("Lives: 3", "white", -280, 280)


# Set Keyboard Bindings
game.set_keyboard_binding(spgl.KEY_UP, player.up)
game.set_keyboard_binding(spgl.KEY_DOWN, player.down)

if player.score > 100:
	banana = Banana("banana.gif", "black", random.randint(100,1000), -130)

while True:
    # Call the game tick method
	game.tick()
	player.score += 1
	score_label.update("Score: {}".format(player.score))
	
	
	if game.is_collision(player, plant):
		player.lives += -1
		lives_label.update("Lives: {}".format(player.lives))
		
		max_x = -400
		for object in objects:
			if object.xcor() > max_x:
				max_x = object.xcor()
		
		plant.goto(random.randint(300,600) + max_x, -100)
		
	if game.is_collision(player, shell):
		player.lives += -1
		lives_label.update("Lives: {}".format(player.lives))
		max_x = -400
		for object in objects:
			if object.xcor() > max_x:
				max_x = object.xcor()
	
		shell.setx(random.randint(600,900) + max_x)

	if game.is_collision(player, coin):
		player.score += 50
		lives_label.update("Lives: {}".format(player.lives))
		
		max_x = -400
		for object in objects:
			if object.xcor() > max_x:
				max_x = object.xcor()
	
		coin.setx(random.randint(600,900) + max_x)

	if game.is_collision(player, banana):
		player.lives += -1
		lives_label.update("Lives: {}".format(player.lives))
		
		max_x = -400
		for object in objects:
			if object.xcor() > max_x:
				max_x = object.xcor()
	
		banana.setx(random.randint(300,600) + max_x)		

# 	if player.xcor() == plant.xcor() and player.xcor() == shell.xcor():
# 		player.score += 1
		
	if plant.xcor() < -500:
		plant.goto(random.randint(300,600), -100)
		
	if shell.xcor() < -500:
		shell.goto(random.randint(600,900), -20)
	
	if coin.xcor() < -500:
		coin.goto(random.randint(600,900), -20)


	if player.score >500:
		plant.speed = -15
		shell.speed = -15
		coin.speed = -15
		banana.speed = -15
		
	if player.score >1000:
		plant.speed = -17
		shell.speed = -17	
		coin.speed = -17
		banana.speed = -17
			
	if player.score >1500:
		plant.speed = -19
		shell.speed = -19	
		coin.speed = -19
		banana.speed = -19
		
# 	if player.lives < 0:
# 		label_name = spgl.Label("GAME OVER", "white", -200, 100)  
# 		label_name.set_font_name("SuperMarioBrosWii")
# 		label_name.set_font_size(50)		