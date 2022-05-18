import numpy as np
import random
import game_graphics

def make_empty_grid():
    grid = np.full((9,9),1)
    print(grid)
    return grid



def make_grid():
    #creates grid
    grid = np.full((9,9),0)
    print(grid)

    # adds bombs at random to grid
    bombs = [""]

    for x in range(9):
        bomb_placed = False
        #makes sure their is no dupes
        while bomb_placed == False:
            n = 0
            x = random.randint(0,8)
            y = random.randint(0,8)
            bomb_pos = str(x) + "," + str(y)
            #makes sure bomb has not been placed
            for i in bombs:
                print(n)
                if bomb_pos == i:
                    pass
                elif bomb_pos != i:
                    n = n + 1
                if n == len(bombs):
                    bombs.append(bomb_pos)
                    print (bombs)
                    grid[x,y] = grid[x,y]+50
                    bomb_placed = True
                
            print (n)   

            print (n)
        #creates the diffrent cords. 1 is postive and 2 is negtive.
        x1 = x + 1
        x2 = x - 1
        y1 = y + 1
        y2 = y - 1

        #checks if y is even. (changes the layout )
        if  y % 2 == 0: 
            #checks all the sides and runs the corrisponding code depending on the bomb placement
            #adds 1 to the surronding tiles of bomb.
                if x == 0:
                    if y == 0:
                        grid[x1,y] = grid[x1,y] + 1
                        grid[x1,y1] = grid[x,y1] + 1
                        grid[x,y1] = grid[x,y1] + 1
                    elif y == 8:
                        grid[x,y2] = grid[x,y2] + 1
                        grid[x1,y2] = grid[x1,y2] + 1
                        grid[x1,y] = grid[x1,y] + 1
                    else: 
                        grid[x,y1] = grid[x,y1] + 1
                        grid[x1,y1] = grid[x1,y1] + 1
                        grid[x1,y] = grid[x1,y] + 1
                        grid[x,y2] = grid[x,y2] + 1
                        grid[x1,y2] = grid[x1,y2] + 1
                       
                elif x == 8: 
                    if y == 0:
                        grid[x2,y] = grid[x2,y] + 1
                        grid[x,y1] = grid[x,y1] + 1
                    elif y == 8:
                        grid[x,y2] = grid[x,y2] + 1
                        grid[x2,y] = grid[x2,y] + 1
                    else: 
                        grid[x,y1] = grid[x,y1] + 1
                        grid[x2,y] = grid[x2,y] + 1
                        grid[x,y2] = grid[x,y2] + 1
        
                elif y == 0:
                    grid[x1,y1]  = grid[x1,y1] + 1
                    grid[x,y1] = grid[x,y1] + 1
                    grid[x1,y] = grid[x1,y] + 1
                    grid[x2,y] = grid[x2,y] + 1
        
                elif y == 8:
                    grid[x1,y2] = grid[x1,y2] + 1
                    grid[x,y2] = grid[x,y2] + 1
                    grid[x1,y] = grid[x1,y] + 1
                    grid[x2,y] = grid[x2,y] + 1
        
                else:
                    grid[x1,y1]  = grid[x1,y1] + 1
                    grid[x1,y2] = grid[x1,y2] + 1
                    grid[x,y1] = grid[x,y1] + 1
                    grid[x,y2] = grid[x,y2] + 1
                    grid[x1,y] = grid[x1,y] + 1
                    grid[x2,y] = grid[x2,y] + 1
    
        elif  y % 2 != 0:    
                if x == 8:
                    grid[x,y1] = grid[x,y1] + 1
                    grid[x2,y] = grid[x2,y] + 1
                    grid[x,y2] = grid[x,y2] + 1
                    grid[x2,y2] = grid[x2,y2] + 1
                    grid[x2,y1] = grid[x2,y1] + 1
                        
                elif x == 0: 
                    grid[x,y2] = grid[x,y2] + 1
                    grid[x1,y] = grid[x1,y] + 1
                    grid[x,y1] = grid[x,y1] + 1
    
                else:
                    grid[x2,y1]  = grid[x2,y1] + 1
                    grid[x2,y2] = grid[x2,y2] + 1
                    grid[x,y1] = grid[x,y1] + 1
                    grid[x,y2] = grid[x,y2] + 1
                    grid[x2,y] = grid[x2,y] + 1
                    grid[x1,y] = grid[x1,y] + 1
    return grid

def check_negibours(x,y,grid,empty_grid):
        x1 = x + 1
        x2 = x - 1
        y1 = y + 1
        y2 = y - 1
        print (x,y)
        if empty_grid[x,y] == 1:
            empty_grid[x, y] = 0
            #topleft corner
            if y == 0 and x == 0:
                # right horozontal
                if grid[x1,y] == 0:
                    empty_grid = check_negibours(x1, y, grid, empty_grid)
                elif grid[x1,y] < 7:
                    empty_grid[x1,y] = 0
                #right bottom
                if grid[x1,y1] == 0:
                    empty_grid = check_negibours(x1, y1, grid, empty_grid)
                elif grid[x1,y1] < 7:
                    empty_grid[x1,y1] = 0
                #left bottom
                if grid[x2, y1] == 0:
                    empty_grid = check_negibours(x, y1, grid, empty_grid)
                elif grid[x, y1] < 7:
                    empty_grid[x, y1] = 0

            # topright corner
            elif y == 0 and x == 8:
                #left horozontal
                if grid[x2, y] == 0:
                    empty_grid = check_negibours(x2, y, grid, empty_grid)
                elif grid[x2, y] < 7:
                    empty_grid[x2, y] = 0
                #left bottom
                if grid[x, y1] == 0:
                    empty_grid = check_negibours(x, y1, grid, empty_grid)
                elif grid[x, y1] < 7:
                    empty_grid[x, y1] = 0

            #toprow
            elif y == 0:
                #right horizontal
                if grid[x1, y] == 0:
                    empty_grid = check_negibours(x1, y, grid, empty_grid)
                elif grid[x1, y] < 7:
                    empty_grid[x1, y] = 0
                #left horizontal
                if grid[x2, y] == 0:
                    empty_grid = check_negibours(x2, y, grid, empty_grid)
                elif grid[x2, y] < 7:
                    empty_grid[x2, y] = 0
                # right bottom
                if grid[x1, y1] == 0:
                    empty_grid = check_negibours(x1, y1, grid, empty_grid)
                elif grid[x1, y1] < 7:
                    empty_grid[x1, y1] = 0
                # left bottom
                if grid[x2, y1] == 0:
                    empty_grid = check_negibours(x, y1, grid, empty_grid)
                elif grid[x, y1] < 7:
                    empty_grid[x, y1] = 0

            #bottomleft corner
            elif y == 8 and x == 0:
                # right horozontal
                if grid[x1,y] == 0:
                    empty_grid = check_negibours(x1, y, grid, empty_grid)
                elif grid[x1,y] < 7:
                    empty_grid[x1,y] = 0
                #right bottom
                if grid[x1,y2] == 0:
                    empty_grid = check_negibours(x1, y2, grid, empty_grid)
                elif grid[x1,y2] < 7:
                    empty_grid[x1,y2] = 0
                #left bottom
                if grid[x1, y2] == 0:
                    empty_grid = check_negibours(x, y2, grid, empty_grid)
                elif grid[x, y2] < 7:
                    empty_grid[x, y2] = 0

            #bottomright corner
            elif y == 8 and x == 8:
                #left horozontal
                if grid[x2, y] == 0:
                    empty_grid = check_negibours(x2, y, grid, empty_grid)
                elif grid[x2, y] < 7:
                    empty_grid[x2, y] = 0
                #left bottom
                if grid[x, y2] == 0:
                    empty_grid = check_negibours(x, y2, grid, empty_grid)
                elif grid[x, y2] < 7:
                    empty_grid[x, y2] = 0

            #bottomrow
            elif y == 8 and x != 0 and x != 8:
                #right top
                if grid[x, y2] == 0:
                    empty_grid = check_negibours(x, y2, grid, empty_grid)
                elif grid[x, y2] < 7:
                    empty_grid[x, y2] = 0
                #left horizontal
                if grid[x2, y] == 0:
                    empty_grid = check_negibours(x2, y, grid, empty_grid)
                elif grid[x2, y] < 7:
                    empty_grid[x2, y] = 0
                #left top
                if grid[x1, y2] == 0:
                    empty_grid = check_negibours(x1, y2, grid, empty_grid)
                elif grid[x1, y2] < 7:
                    empty_grid[x1, y2] = 0
                #right horizontal
                if grid[x1, y] == 0:
                    empty_grid = check_negibours(x1, y, grid, empty_grid)
                elif grid[x1, y] < 7:
                    empty_grid[x1, y] = 0

            #leftside
            elif x == 0 and y != 0 and y != 8:
                if  y % 2 == 0:
                    # right horozontal
                    if grid[x1,y] == 0:
                        empty_grid = check_negibours(x1, y, grid, empty_grid)
                    elif grid[x1,y] < 7:
                        empty_grid[x1,y] = 0
                    #right bottom
                    if grid[x1,y1] == 0:
                        empty_grid = check_negibours(x1, y1, grid, empty_grid)
                    elif grid[x1,y1] < 7:
                        empty_grid[x1,y1] = 0
                    #left bottom
                    if grid[x, y1] == 0:
                        empty_grid = check_negibours(x, y1, grid, empty_grid)
                    elif grid[x, y1] < 7:
                        empty_grid[x, y1] = 0
                    # right top
                    if grid[x1, y2] == 0:
                        empty_grid = check_negibours(x1, y2, grid, empty_grid)
                    elif grid[x1, y2] < 7:
                        empty_grid[x1, y2] = 0
                    # left top
                    if grid[x, y2] == 0:
                        empty_grid = check_negibours(x, y2, grid, empty_grid)
                    elif grid[x, y2] < 7:
                        empty_grid[x, y2] = 0

                if  y % 2 != 0:
                    # right horozontal
                    if grid[x1,y] == 0:
                        empty_grid = check_negibours(x, y, grid, empty_grid)
                    elif grid[x1,y] < 7:
                        empty_grid[x1,y] = 0
                    #right bottom
                    if grid[x,y1] == 0:
                        empty_grid = check_negibours(x, y1, grid, empty_grid)
                    elif grid[x,y1] < 7:
                        empty_grid[x,y1] = 0
                    # right top
                    if grid[x, y2] == 0:
                        empty_grid = check_negibours(x, y2, grid, empty_grid)
                    elif grid[x, y2] < 7:
                        empty_grid[x, y2] = 0

            #rightside
            elif x == 8:
                if  y % 2 == 0:
                    # right horozontal
                    if grid[x,y2] == 0:
                        empty_grid = check_negibours(x, y2, grid, empty_grid)
                    elif grid[x,y2] < 7:
                        empty_grid[x,y2] = 0
                    #right bottom
                    if grid[x,y1] == 0:
                        empty_grid = check_negibours(x, y1, grid, empty_grid)
                    elif grid[x,y1] < 7:
                        empty_grid[x,y1] = 0
                    #right top
                    if grid[x2, y] == 0:
                        empty_grid = check_negibours(x2, y, grid, empty_grid)
                    elif grid[x2, y] < 7:
                        empty_grid[x2, y] = 0
                    

                if  y % 2 != 0:
                    # right horozontal
                    if grid[x2,y] == 0:
                        empty_grid = check_negibours(x2, y, grid, empty_grid)
                    elif grid[x2,y] < 7:
                        empty_grid[x2,y] = 0
                    #right bottom
                    if grid[x,y1] == 0:
                        empty_grid = check_negibours(x, y1, grid, empty_grid)
                    elif grid[x,y1] < 7:
                        empty_grid[x,y1] = 0
                    # right top
                    if grid[x, y2] == 0:
                        empty_grid = check_negibours(x, y2, grid, empty_grid)
                    elif grid[x, y2] < 7:
                        empty_grid[x, y2] = 0
                    #left bottom
                    if grid[x2, y1] == 0:
                        empty_grid = check_negibours(x2, y1, grid, empty_grid)
                    elif grid[x2, y1] < 7:
                        empty_grid[x, y1] = 0
                    # left top
                    if grid[x2, y2] == 0:
                        empty_grid = check_negibours(x2, y2, grid, empty_grid)
                    elif grid[x2, y2] < 7:
                        empty_grid[x2, y2] = 0
            #even mid
            elif  y % 2 == 0:
                    # right horozontal
                    if grid[x1,y] == 0:
                        empty_grid = check_negibours(x1, y, grid, empty_grid)
                    elif grid[x1,y] < 7:
                        empty_grid[x1,y] = 0
                    #right bottom
                    if grid[x1,y1] == 0:
                        empty_grid = check_negibours(x1, y1, grid, empty_grid)
                    elif grid[x1,y1] < 7:
                        empty_grid[x1,y1] = 0
                    # right top
                    if grid[x1, y2] == 0:
                        empty_grid = check_negibours(x1, y2, grid, empty_grid)
                    elif grid[x1, y2] < 7:
                        empty_grid[x1, y2] = 0
                    #left bottom
                    if grid[x, y1] == 0:
                        empty_grid = check_negibours(x, y1, grid, empty_grid)
                    elif grid[x, y1] < 7:
                        empty_grid[x, y1] = 0
                    # left top
                    if grid[x, y2] == 0:
                        empty_grid = check_negibours(x, y2, grid, empty_grid)
                    elif grid[x, y2] < 7:
                        empty_grid[x, y2] = 0
                    #left horizontal
                    if grid[x2, y] == 0:
                        empty_grid = check_negibours(x2, y, grid, empty_grid)
                    elif grid[x2, y] < 7:
                        empty_grid[x2, y] = 0

            #odd mid
            elif  y % 2 != 0:
                    # right horozontal
                    if grid[x1,y] == 0:
                        empty_grid = check_negibours(x1, y, grid, empty_grid)
                    elif grid[x1,y] < 7:
                        empty_grid[x1,y] = 0
                    #right bottom
                    if grid[x,y1] == 0:
                        empty_grid = check_negibours(x, y1, grid, empty_grid)
                    elif grid[x,y1] < 7:
                        empty_grid[x,y1] = 0
                    # right top
                    if grid[x, y2] == 0:
                        empty_grid = check_negibours(x, y2, grid, empty_grid)
                    elif grid[x, y2] < 7:
                        empty_grid[x, y2] = 0
                    #left bottom
                    if grid[x2, y1] == 0:
                        empty_grid = check_negibours(x2, y1, grid, empty_grid)
                    elif grid[x2, y1] < 7:
                        empty_grid[x2, y1] = 0
                    # left top
                    if grid[x2, y2] == 0:
                        empty_grid = check_negibours(x2, y2, grid, empty_grid)
                    elif grid[x2, y2] < 7:
                        empty_grid[x2, y2] = 0
                    #left horizontal
                    if grid[x2, y] == 0:
                        empty_grid = check_negibours(x2, y, grid, empty_grid)
                    elif grid[x2, y] < 7:
                        empty_grid[x2, y] = 0
       
        return empty_grid


        
def end():
    #ends the program
    quit()

        
    
def check_grid(x,y,empty_grid,grid,screen):
    #sees if bombs been pressed
    if grid[x, y] >= 50:
        game_graphics.end(screen)
    #if it next to a bomb (has a number) it removes the button on that title only.
    elif grid[x, y] > 0:
        empty_grid[x, y] = 0
        print("0")
    #if it is empty it removes the button on that title and surrounding titles until the borders are numbers or edge of grid
    elif grid[x, y] == 0:
        empty_grid = check_negibours(x, y, grid, empty_grid)
    return empty_grid
