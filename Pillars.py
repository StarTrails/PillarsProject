"""Imports needed modules for code to function"""
import pygame
import random

pygame.init()

"""Specifies what images to use and defines their name"""
TileSet = {
'TileDesert' : pygame.image.load("Desert_Tile.png"),
'TileGrass' : pygame.image.load("Grass_Tile.png"),
'TileHill' : pygame.image.load("Hill_Tile.png")
}

"""Creates a list of all images defined"""
TileList = ['TileDesert', 'TileGrass', 'TileHill']

"""Sets the screen width and heights and also defines tilesize"""
TILESIZE = 140
MAPWIDTH = 840
MAPHEIGHT = 700


MAINSCREEN = pygame.display.set_mode((840,700))

Odd_Row = MAPWIDTH

"""Creates the loop that generates random terrain"""
GameCycle = True
while GameCycle:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameCycle = False
        if event.type == pygame.KEYDOWN and pygame.K_RETURN:
            for x in range(0, MAPWIDTH, TILESIZE):
                for y in range(0, MAPHEIGHT, TILESIZE):
                    key = TileList[random.randint(0, len(TileList) - 1)]
                    MAINSCREEN.blit(TileSet[key], (x, y))


            pygame.display.flip()