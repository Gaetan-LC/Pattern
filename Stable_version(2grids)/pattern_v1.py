import pygame,sys
from random import *
#from grids import *

width=10
heigh=10

def create_grid(width,heigh):
    grid=[]
    for i in range (heigh):
        grid.append([])
        for j in range (width):
            grid[i].append(2)
    return grid
grid=create_grid(width,heigh)
print(grid)
print(len(grid))

def print_grid(grid):
    for i in range (len(grid)):
        print(grid[i])

print_grid(grid)

def full_grid(grid):
    if randint(0,3)>=2: #def [0;0]
        grid[0][0]=1
    else:
        grid[0][0]=0
        
    for c in range (1,len(grid[0])): #def 1st line
        if grid[0][c-1]==1:
            if randint(0,3)>=1:
                grid[0][c]=1
            else:
                grid[0][c]=0
        else:
            if randint(0,3)>=3:
                grid[0][c]=1
            else:
                grid[0][c]=0

    for l in range (1,len(grid)): #def collumn 1
        if grid[l-1][0]==1:
            if randint(0,3)>=1:
                grid[l][0]=1
            else:
                grid[l][0]=0
        else:
            if randint(0,3)>=3:
                grid[l][0]=1
            else:
                grid[l][0]=0

    for l in range (1,len(grid)): #def all other squares
        for c in range (1,len(grid[0])):
            if grid[l-1][c]==1 and grid[l][c-1]==1:
                if randint(0,3)>=1:
                    grid[l][c]=1
                else:
                    grid[l][c]=0
            if grid[l-1][c]==1 and grid[l][c-1]==0 or grid[l-1][c]==0 and grid[l][c-1]==1:
                if randint(0,3)>=2:
                    grid[l][c]=1
                else:
                    grid[l][c]=0
            if grid[l-1][c]==0 and grid[l][c-1]==0:
                if randint(0,3)>=3:
                    grid[l][c]=1
                else:
                    grid[l][c]=0
    return grid

full_grid=full_grid(grid)
print_grid(full_grid)



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
            for l in range(len(grid)) :
                for c in range(len(grid[0])):
                    if grid[l][c] == 0 :
                        pygame.draw.rect(screen,[255,255,255],(l*sizeY,c*sizeX,sizeY,sizeX))
                    if grid[l][c] == 1 :
                        pygame.draw.rect(screen,[0,0,0],(l*sizeY,c*sizeX,sizeY,sizeX))                    
                    if grid[l][c] == 2 :
                        pygame.draw.rect(screen,[255,0,0],(l*sizeY,c*sizeX,sizeY,sizeX))
            gamemode=2
            pygame.display.flip()

