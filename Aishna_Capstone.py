# SPGL Minimal Code by /u/wynand1004 AKA @TokyoEdTech
# Requires SPGL Version 0.8 or Above
# SPGL Documentation on Github: https://wynand1004.github.io/SPGL
# Use this as the starting point for your own games

# Import SPGL
import spgl
import random
import os
import time

# Create Classes

# class Game(spgl.Sprite):
# 	def __init__(self, shape, color, x, y):
# 		spgl.Sprite.__init__(self, shape, color, x, y)
# 		game.play_sound("bg_sound.wav")



				
class Player(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)
		self.frame = 0
		self.y_acceleration = 5
		self.y_speed = 5
		self.strength = 7
		self.score = 0
		self.state = "running"
		self.lives = 5
	
	def up(self):
		if self.state == "running" or self.state == "crouching":
			self.y_acceleration += self.strength
			game.play_sound("jump.wav")
			self.set_image("mario_jump.gif", 90, 116)
			self.sety(0)
			self.state = "jumping"
			
	
	def down(self):
		if self.state != "jumping":
			self.sety(-105)
			self.set_image("Mario_Crouch.gif", 150, 100)
			self.state = "crouching"
				
	def tick(self):
		self.setx(self.xcor())
		
		if self.ycor() < -80:
			self.y_acceleration = 1
			self.y_speed = 1
			self.sety(-95) 
			if self.state != "running" and self.state != "crouching":
				self.state = "running"
				self.set_image("mario_run.gif", 90, 116)			
			if self.state == "crouching":
				self.sety(-95)
			
		self.y_acceleration += game.gravity
		self.y_speed += self.y_acceleration
		self.sety(self.ycor() + self.y_speed)

class Plant(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)	
		self.frame = 0
		self.speed = -13
		self.shape("plant.gif")

	def tick(self):
		self.fd(self.speed)

class Shell(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)	
		self.frame = 0
		self.speed = -13
	def tick(self):
		self.fd(self.speed)

class Coin(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)	
		self.frame = 0
		self.speed = -13
		self.shape("coin.gif")

	def tick(self):
		self.fd(self.speed)

class Banana(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)	
		self.frame = 0
		self.speed = -13
		self.shape("banana.gif")
		self.state = "ready"

	def tick(self):
		if self.state == "active":
			self.fd(self.speed)

class Goomba(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)	
		self.frame = 0
		self.speed = -13
		self.shape("goomba.gif")
		self.state = "ready"

	def tick(self):
		if self.state == "active":
			self.fd(self.speed)

class Brick(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)
		self.frame = 0
		self.speed = -13
		self.shape("brick.gif")
	
	def tick(self):
		self.fd(self.speed)

class Mushroom(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)
		self.frame = 0
		self.speed = -13
		self.shape("mushroom.gif")

	def tick(self):
		self.fd(self.speed)

def end_game():
	game.stop_all_sounds()
	os._exit(1)

# Initial Game setup
game = spgl.Game(800, 600, "black", "Aishna Capstone Project", 1)
game.gravity = -1.15

# Create Sprites

# title = Game("supermario.gif", "green", 10, 200)

player = Player("mario_run.gif", "blue", -200, -100)
player.set_image("mario_run.gif", 58, 50)

shell = Shell("shell.gif", "red",random.randint(300,1000), -6)
shell.set_image("shell.gif",53, 55)

plant = Plant("plant.gif", "white", random.randint(100,1000), -100)
plant.set_image("plant.gif", 49, 24)

coin = Coin("coin.gif", "white", random.randint(100,1000), -6)
coin.set_image("coin.gif", 35, 33)

banana = Banana("banana.gif", "black", random.randint(450,1000), -130)
banana.set_image("banana.gif", 54, 57)

brick = Brick("brick.gif", "white", random.randint(800, 1000), 5)
brick.set_image("brick.gif", 60, 10)

mushroom = Mushroom("mushroom.gif", "white", random.randint(800, 1000), 5)
mushroom.set_image("mushroom.gif", 60, 10)

goomba = Goomba("goomba.gif", "black", random.randint(600,1000), -120)
goomba.set_image("goomba.gif", 54, 57)

objects = [shell, plant, coin, banana, brick]


score_label = spgl.Label("Score: 0", "white", -380, 260)
score_label.set_font_size(20)
lives_label = spgl.Label("Lives: 5", "white", -270, 260)
lives_label.set_font_size(20)


# Set Keyboard Bindings
game.set_keyboard_binding(spgl.KEY_UP, player.up)
game.set_keyboard_binding(spgl.KEY_DOWN, player.down)
game.set_keyboard_binding("q", end_game)


game.set_background("ground.gif")
game.play_sound("bg_sound.wav")



while True:
    # Call the game tick method
	game.tick()
	player.score += 1
	if player.score % 30 == 0:
		score_label.update("Score: {}".format(player.score))
	
	
	if game.is_collision(player, plant):
		player.lives += -1
		lives_label.update("Lives: {}".format(player.lives))
		
		max_x = -400
		for object in objects:
			if object.xcor() > max_x:
				max_x = object.xcor()
		
		plant.goto(random.randint(400,600) + max_x, -100)
		
	if game.is_collision(player, shell):
		player.lives += -1
		lives_label.update("Lives: {}".format(player.lives))
		max_x = -400
		for object in objects:
			if object.xcor() > max_x:
				max_x = object.xcor()
	
		shell.setx(random.randint(600,900) + max_x)

	if game.is_collision(player, coin):
		game.play_sound("coin_sound.wav")
		player.score += 50
		score_label.update("Lives: {}".format(player.score))
		
		max_x = -400
		for object in objects:
			if object.xcor() > max_x:
				max_x = object.xcor()	
		coin.setx(random.randint(800,900) + max_x)

	if game.is_collision(player, banana):
		player.lives += -1
		lives_label.update("Lives: {}".format(player.lives))
		
		max_x = -400
		for object in objects:
			if object.xcor() > max_x:
				max_x = object.xcor()
		banana.setx(random.randint(450,1000) + max_x)		

	if game.is_collision(player, goomba):
		player.lives += -1
		lives_label.update("Lives: {}".format(player.lives))
		
		max_x = -400
		for object in objects:
			if object.xcor() > max_x:
				max_x = object.xcor()
		goomba.setx(random.randint(600,1000) + max_x)

	if game.is_collision(player, brick):
		player.lives += 1
		lives_label.update("Lives: {}".format(player.lives))
		max_x = -400
		for object in objects:
			if object.xcor() > max_x:
				max_x = object.xcor()
		brick.setx(random.randint(800,1000) + max_x)
		
	if plant.xcor() < -500:
		plant.goto(random.randint(300,600), -100)
		
	if shell.xcor() < -500:
		shell.goto(random.randint(600,900), -20)
	
	if coin.xcor() < -500:
		coin.goto(random.randint(800,900), -10)

# 	if banana.xcor() < -500:
# 		banana.goto(random.randint(300,600), -100)

	if brick.xcor() < -500:
		brick.goto(random.randint(800,1000), -20)


	if player.score >= 1000:
		goomba.state = "active"

	if player.score >500:
		plant.speed = -15
		shell.speed = -15
		coin.speed = -15
		banana.speed = -15
		goomba.speed = -15
		mushroom.speed = -15
		brick.speed = -15

	if player.score >1000:
		plant.speed = -16
		shell.speed = -16	
		coin.speed = -16
		banana.speed = -16
		goomba.speed = -16
		mushroom.speed = -16
		brick.speed = -16
		
	if player.score >1500:
		plant.speed = -18
		shell.speed = -18	
		coin.speed = -18
		banana.speed = -18
		goomba.speed = -18
		mushroom.speed = -18
		brick.speed = -18
		
	if player.score >2000:
		plant.speed = -19
		shell.speed = -19	
		coin.speed = -19
		banana.speed = -19
		goomba.speed = -19
		mushroom.speed = -19
		brick.speed = -19

	if player.score > 500 and banana.state != "active":
		max_x = -400
		for object in objects:
			if object.xcor() > max_x:
				max_x = object.xcor()
		banana.state = "active"
		banana.setx(random.randint(450,1000) + max_x)		

		
	if player.score > 1000:
		max_x = -400
		for object in objects:
			if object.xcor() > max_x:
				max_x = object.xcor()
		goomba.state = "active"
		goomba.setx(random.randint(600,1000) + max_x)
		
	if game.is_collision(player, brick):
		mushroom.goto(400, 4)

	if player.lives == 0:
		game.set_background("game_over.gif")
	


