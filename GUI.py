
screen = 0
import sys

def setup():
	global title_font
	global button_font
	global detail_font
	size(900,650)
	strokeWeight(2)
	title_font = createFont("Arial", 50)
	button_font = createFont("Arial", 32)
	detail_font = createFont("Arial", 22)

def draw():

	global title_font
	global button_font
	global detail_font
	global screen
	rectMode(CENTER)

	if (screen == 0):

		background(200)
		fill(100)
		rect(150,315,270,100)
		rect(450,315,270,100)
		rect(750,315,270,100)
		fill(200,0,0)
		rect(875,25,50,50)

		textFont(title_font)
		fill(0)
		textAlign(CENTER)
		text("Festival Bros", 450, 50)

		textFont(button_font)
		text("Find Festivals\nNear Me", 150, 300)
		text("Create a Custom\nFestival Schedule", 450, 300)
		text("Randomize a\nFestival Schedule", 750, 300)

		textFont(button_font)
		text("Welcome!", 450, 100)

		textFont(detail_font)
		text("X",875,35)

		if (mousePressed and mouseX > 15 and mouseX < 285 and mouseY > 265 and mouseY < 365):
			screen = 1
		if (mousePressed and mouseX > 315 and mouseX < 585 and mouseY > 265 and mouseY < 365):
			screen = 2
		if (mousePressed and mouseX > 615 and mouseX < 885 and mouseY > 265 and mouseY < 365):
			screen = 3
		if (mousePressed and mouseX > 850 and mouseX < 900 and mouseY > 0 and mouseY < 50):
			sys.exit()

	if (screen == 1):
		background(200)
		textFont(title_font)
		fill(0)
		textAlign(CENTER)
		text("Festivals Near Me", 450, 50)

		fill(50,200,50)
		rect(825,40,120,25)

		fill(0)
		textFont(detail_font)
		text("Main Menu",825,50)

		if (mousePressed and mouseX > 800 and mouseX < 850 and mouseY > 15 and mouseY < 65):
			screen = 0

	if (screen == 2):
		background(200)
		textFont(title_font)
		fill(0)
		textAlign(CENTER)
		text("Festival Scheduler", 450, 50)

		fill(50,200,50)
		rect(825,40,120,25)

		fill(0)
		textFont(detail_font)
		text("Main Menu",825,50)

		if (mousePressed and mouseX > 800 and mouseX < 850 and mouseY > 15 and mouseY < 65):
			screen = 0

	if (screen == 3):
		background(200)
		textFont(title_font)
		fill(0)
		textAlign(CENTER)
		text("Schedule Randomizer", 450, 50)

		fill(50,200,50)
		rect(825,40,120,25)

		fill(0)
		textFont(detail_font)
		text("Main Menu",825,50)

		if (mousePressed and mouseX > 800 and mouseX < 850 and mouseY > 15 and mouseY < 65):
			screen = 0





















	