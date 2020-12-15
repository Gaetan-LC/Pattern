import pygame,sys
from random import *
from grids import *

#-------------------------------------------------------------
#-------------------------------------------------------------
running = True
gamemode=1
sizeX=100
sizeY=100
win_length=width*sizeX
win_heigh=heigh*sizeY
#print("sizeX",sizeX,"\nsizeY",sizeY,"\nwin_length",win_length,"\nwin_heigh",win_heigh)
pygame.init()
screen = pygame.display.set_mode((win_length,win_heigh))
pygame.display.set_caption("Pattern")

while running:
    screen.fill((0,255,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if gamemode==1:
            for l in range(len(grid)) :
                for c in range(len(grid[0])):
                    if grid[l][c][1] == 0 :
                        pygame.draw.rect(screen,[255,255,255],(c*sizeX,l*sizeY,sizeX,sizeY))
                    if grid[l][c][1] == 1 :
                        pygame.draw.rect(screen,[0,0,0],(c*sizeX,l*sizeY,sizeX,sizeY))                    
                    if grid[l][c][1] == 2 :
                        pygame.draw.rect(screen,[100,100,100],(c*sizeX,l*sizeY,sizeX,sizeY))
            gamemode=2
            pygame.display.flip()

