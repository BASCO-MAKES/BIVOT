import pygame
import math

from transform import Transform

FPS = 100
magRadius = 90
clock = pygame.time.Clock()

game_run = True
rotateMag = False
rectangle = Transform((0,0),[(40,90),(255,0,0)])

bg_img = pygame.image.load("./Images/Background.png")
windowSize = bg_img.get_size()

knob_img = pygame.image.load("./Images/Knob.png")
sensors_img = pygame.image.load("./Images/Sensors.png")

mag_img = pygame.image.load("./Images/Magnet.png")
magClick_img = pygame.image.load("./Images/Magnet_Clicked.png")

mag = Transform((0,0),mag_img)

sensors_Size = sensors_img.get_size()
sensors_pos = ((windowSize[0]-sensors_Size[0])/2,(windowSize[1]-sensors_Size[1])/2)
sensors = Transform(sensors_pos,sensors_img)

knobSize = knob_img.get_size()
knobPos = ((windowSize[0]-knobSize[0])//2,(windowSize[1]-knobSize[1])//2)
knob = Transform(knobPos,knob_img)


window = pygame.display.set_mode(windowSize)
pygame.display.set_caption("First Game")

def Setup():

	return 0

def Update():

	if(rotateMag):
		mag.position = CalculateMagPos(pygame.mouse.get_pos(),magRadius)



	DrawFrame()
	pygame.display.update()

	return 0

def DrawFrame():
	global rectangle
	window.blit(bg_img,(0,0))
	DrawObject(sensors)
	DrawObject(knob)

	DrawObject(mag)

def DrawObject(object:Transform):
	window.blit(object.image,object.position)
	
def CheckEvents():
	global game_run,rectangle,rotateMag
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_run = False

		if event.type == pygame.MOUSEMOTION:
			rectangle.position = pygame.mouse.get_pos()

		if event.type == pygame.MOUSEBUTTONDOWN:
			rotateMag = True
			mag.image = magClick_img
		if event.type == pygame.MOUSEBUTTONUP:
			rotateMag = False
			mag.image = mag_img
		
			
		
def CalculateMagPos(mousePos:tuple, radius):
	windowSize = window.get_size()
	
	center = (windowSize[0]//2,windowSize[1]//2)
	
	MouseRelPos = (mousePos[0]-center[0],mousePos[1]-center[1])
	dist = math.sqrt(MouseRelPos[1]**2+MouseRelPos[0]**2)

	ratio = radius/dist
	magCenterPos = (MouseRelPos[0]*ratio+center[0],MouseRelPos[1]*ratio+center[1])
	global mag_img
	size = mag_img.get_size()
	magPos = (magCenterPos[0]-size[0]//2,magCenterPos[1]-size[1]//2)
	return magPos

if __name__ == "__main__":

	Setup()

	while game_run:
		clock.tick(FPS)
		CheckEvents()
		Update()
		
	

pygame.quit()
