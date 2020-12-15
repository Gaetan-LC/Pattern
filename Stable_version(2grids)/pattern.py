import pygame,sys
from random import *
from grids import *

#-------------------------------------------------------------
#-------------------------------------------------------------
running = True
gamemode=1
win_length=500
win_heigh=500
sizeX=win_length/width
sizeY=win_heigh/heigh

pygame.init()
screen = pygame.display.set_mode((win_length,win_heigh))
pygame.display.set_caption("Pattern")

while running:
    screen.fill((0,255,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if gamemode==1:
            for l in range(len(p_grid)) :
                for c in range(len(p_grid[0])):
                    if p_grid[l][c] == 0 :
                        pygame.draw.rect(screen,[255,255,255],(l*sizeY,c*sizeX,sizeY,sizeX))
                    if p_grid[l][c] == 1 :
                        pygame.draw.rect(screen,[0,0,0],(l*sizeY,c*sizeX,sizeY,sizeX))                    
                    if p_grid[l][c] == 2 :
                        pygame.draw.rect(screen,[100,100,100],(l*sizeY,c*sizeX,sizeY,sizeX))
            gamemode=2
            pygame.display.flip()

