from random import *
width=5
heigh=5
def create_grid(width,heigh):
    grid=[]
    for i in range (heigh):
        grid.append([])
        for j in range (width):
            grid[i].append([2,2])
    
    #Create back level

    if randint(0,3)>=2: #def [0;0]2nd layer
        grid[0][0][1]=1
    else:
        grid[0][0][1]=0

    for c in range (1,len(grid[0])): #def 1st line
        if grid[0][c-1][1]==1:
            if randint(0,3)>=1:
                grid[0][c][1]=1
            else:
                grid[0][c][1]=0
        else:
            if randint(0,3)>=3:
                grid[0][c][1]=1
            else:
                grid[0][c][1]=0

    for l in range (1,len(grid)): #def collumn 1
        if grid[l-1][0][1]==1:
            if randint(0,3)>=1:
                grid[l][0][1]=1
            else:
                grid[l][0][1]=0
        else:
            if randint(0,3)>=3:
                grid[l][0][1]=1
            else:
                grid[l][0][1]=0

    for l in range (1,len(grid)): #def all other squares
        for c in range (1,len(grid[0])):
            if grid[l-1][c][1]==1 and grid[l][c-1][1]==1:
                if randint(0,3)>=1:
                    grid[l][c][1]=1
                else:
                    grid[l][c][1]=0
            if grid[l-1][c][1]==1 and grid[l][c-1][1]==0 or grid[l-1][c][1]==0 and grid[l][c-1][1]==1:
                if randint(0,3)>=2:
                    grid[l][c][1]=1
                else:
                    grid[l][c][1]=0
            if grid[l-1][c][1]==0 and grid[l][c-1][1]==0:
                if randint(0,3)>=3:
                    grid[l][c][1]=1
                else:
                    grid[l][c][1]=0

    return grid

def print_grid(grid):
    for l in range (len(grid)):
        for c in range(len(grid[0])):
            print (grid[l][c][1],end='')
        print()

def numbers(grid):
    num1=[]
    for c in range(len(grid[0])):
        num1.append([])
    a=0
    for c in range(len(grid[0])):
        for l in range(len(grid)):
            if grid[l][c][1]==1:
                a+=1
            if grid[l][c][1]==0 and a!=0:
                num1[c].append(a)
                a=0
        if a!=0:
            num1[c].append(a)
            a=0

    num2=[]
    for l in range(len(grid)):
        num2.append([])
    a=0
    for l in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[l][c][1]==1:
                a+=1
            if grid[l][c][1]==0 and a!=0:
                num2[l].append(a)
                a=0
        if a!=0:
            num2[l].append(a)
            a=0
    
    
    return num1,num2

grid=create_grid(width,heigh)
print_grid(grid)
n1=numbers(grid)[0]
n2=numbers(grid)[1]

print("num1",n1,"\nnum2",n2)