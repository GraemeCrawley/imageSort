import pygame
import time
import os
import shutil
In=1
pygame.init()
w = 1280
h = 1280
size=(w,h)
screen = pygame.display.set_mode(size) 
ball = pygame.Rect(0,0,10,10)

while True:
	imageLocation = raw_input('Please enter the location of the pictures: ')
	sortingFolder = raw_input('Please enter the location of the folder to sort to: ')
	for i in os.listdir(imageLocation):
		screen.fill((0,0,0))
		pygame.display.flip()
		if i.endswith(".jpg") or i.endswith(".png") or i.endswith(".jpeg"):
			print i
			img=pygame.image.load(imageLocation + "/" +i)
			img=pygame.transform.scale(img, (1280, 720))
			screen.blit(img,(0,0))
			pygame.display.flip()
			yesOrNo = raw_input('Should this go in the folder?')

			if yesOrNo=="y":
				shutil.copy(imageLocation + "/" +i,sortingFolder)
			
    