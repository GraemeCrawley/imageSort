import pygame
from pygame.locals import *
import pygame.time
import os
from os.path import dirname, realpath, abspath
import shutil
from array import *

# Define window parameters
gray = (136, 139, 141)
w = 1200
h = 900

# Set up pygame window
pygame.init()
screen = pygame.display.set_mode((w, h))
screen.fill((gray))
pygame.display.flip()


# Image sort loop
# For each image in the unsorted folder, ask the user which folder to sort into
# Blank = leave it unsorted
# 0 = delete
# X = quit loop
running = 1
while running:
	# Get unsorted picture location and sorted locations
	imageLocation = input('Please enter the location of the unsorted pictures: ')
	sortingFolder1 = input('Please enter the location of sorting folder 1: ')
	sortingFolder2 = input('Please enter the location of sorting folder 2: ')
	sortingFolder3 = input('Please enter the location of sorting folder 3: ')

	# Main loop
	for i in os.listdir(imageLocation):
		# Initialize pygame window so that it doesn't crash itself
		pygame.event.wait() 
		screen.fill((gray))
		pygame.display.flip()

		# Load new image and resize to fit
		print("--------")
		print(i)
		img_path = imageLocation + "\\" + i
		img = pygame.image.load(img_path)
		img = pygame.transform.scale(img, (w,h))

		# Place new image into pygame window at 0,0
		screen.fill((gray))
		screen.blit(img,(0,0))
		pygame.display.flip()

		# Prompt the user on where it goes
		whichFolder = input('Which sorting location should it go into? (0 to delete, X to quit): ')

		# React based on user input
		if whichFolder == "1":
			print(sortingFolder1)
			print("Copying...")
			shutil.copy(img_path, sortingFolder1)
			print("Copy complete")

		if whichFolder == "2":
			print(sortingFolder2)
			print("Copying...")
			shutil.copy(img_path, sortingFolder2)
			print("Copy complete")

		if whichFolder == "3":
			print(sortingFolder3)
			print("Copying...")
			shutil.copy(img_path, sortingFolder3)
			print("Copy complete")

		if whichFolder == "0":
			print("Deleting...")
			os.remove(img_path)
			print("Delete complete")
			
		if (whichFolder == "X") or (whichFolder == "x"):
			quit()

		# Clear out img variable
		img = None

	# Ask user if we're doing this again
	goAgain = input("All images sorted.  Go again, Y/N? ")
	if (goAgain == "Y") or (goAgain == "y"):
		running = 1
	if (goAgain == "N") or (goAgain == "n"):
		running = 0

