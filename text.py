# реалізував два окремих об'єкти з текстамИ, які 'бігають' по екрану
import pygame
pygame.init()

size = (600,500)

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Моя програма')
img = pygame.image.load('my_image.jpg')
pygame.display.set_icon(img)

font = pygame.font.SysFont('arial', 32)
YELLOW = (255,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)

text1 = font.render('Текст1', 1, (90,34,76), (0, 255, 0))
text2 = font.render('Текст2', 0, YELLOW, BLUE)
width, height = text2.get_size()
width1, height1 = text1.get_size()
x,y = 90,80
x1,y1 = 0,0
direct_x = 1 
direct_y = 1
direct_x1 = 1
direct_y1 =1
FPS = 60
clock = pygame.time.Clock()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit()
	clock.tick(FPS)
	screen.fill(BLACK)
	screen.blit(text1, (x1, y1))
	screen.blit(text2, (x,y))
	x+=direct_x
	if x+width>=600 or x<0:
		direct_x = -direct_x	
	y+=direct_y
	if y+height>=500 or y<0:
		direct_y = -direct_y

	#text1
	x1+=direct_x1
	if x1+width1>=600 or x1<0:
		direct_x1 = -direct_x1	
	y1+=direct_y1
	if y1+height1>=500 or y1<0:
		direct_y1 = -direct_y1
	pygame.display.update()