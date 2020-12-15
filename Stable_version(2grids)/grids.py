from random import *
width=10
heigh=10
def create_grid(width,heigh):
    grid=[]
    for i in range (heigh):
        grid.append([])
        for j in range (width):
            grid[i].append(2)
    return grid

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

def print_grid(grid):
    for i in range (0,len(grid)):
        print(grid[i])

p_grid=create_grid(width,heigh)
o_grid=create_grid(width,heigh)

o_grid=full_grid(o_grid)

print_grid(o_grid)
print("\n\n\n")
print_grid(p_grid)