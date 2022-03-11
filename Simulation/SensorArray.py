import pygame
from transform import Transform


window = pygame.display.set_mode((500,500))
pygame.display.set_caption("First Game")
FPS = 100
game_run = True
rectangle = Transform((0,0),0,(1,1),[(40,90),(255,0,0)])

bg_img = pygame.image.load('')


def Setup():

	return 0

def Update():

	pygame.time.delay(1000//FPS)


	DrawFrame()
	pygame.display.update()

	return 0

def DrawFrame():
	global rectangle
	window.fill((0,0,0))
	pygame.draw.rect(window,rectangle.object[1],rectangle.position+rectangle.object[0])
def CheckEvents():
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			global game_run
			game_run = False
		if event.type == pygame.MOUSEMOTION:
			global rectangle
			rectangle.position = pygame.mouse.get_pos()
		

if __name__ == "__main__":

	Setup()

	while game_run:

		CheckEvents()
		Update()
		
	

pygame.quit()
