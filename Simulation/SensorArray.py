import pygame

from transform import Transform


window = pygame.display.set_mode((500,500))
pygame.display.set_caption("First Game")

FPS = 100
clock = pygame.time.Clock()

game_run = True
rectangle = Transform((0,0),0,(1,1),[(40,90),(255,0,0)])

bg_img = pygame.image.load("./Images/Background.png")
knob_img = pygame.image.load("./Images/Knob.png")
sensor1_img = pygame.image.load("./Images/Sensor.png")
sensor2_img = pygame.image.load("./Images/Sensor.png")

sensor1 = Transform((0,0),0,(1,1),sensor1_img)
sensor2 = Transform((0,0),0,(1,1),sensor2_img)
knob = Transform((0,0),0,(1,1),knob_img)

pygame.make

def Setup():

	return 0

def Update():

	


	DrawFrame()
	pygame.display.update()

	return 0

def DrawFrame():
	global rectangle
	window.fill((0,0,0))
	#pygame.draw.rect(window,rectangle.image[1],rectangle.position+rectangle.image[0])
	DrawObject(sensor1)

def RotateObject(object:Transform,angle:int):
	image = object.image
	rotated = pygame.transform.rotate(object.image,angle)
	object.image = rotated
	object.rotation+=angle

	
	window.blit(object.image,object.position)

def DrawObject(object:Transform):
	window.blit(object.image,object.position)
	
def CheckEvents():
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			global game_run
			game_run = False
		if event.type == pygame.MOUSEMOTION:
			global rectangle
			rectangle.position = pygame.mouse.get_pos()
		if event.type == pygame.MOUSEBUTTONDOWN:
			#RotateObject(sensor1,45)
			print(sensor1.image.get_height())
			#DrawObject(sensor1)
		

if __name__ == "__main__":

	Setup()

	while game_run:
		clock.tick(FPS)
		CheckEvents()
		Update()
		
	

pygame.quit()
