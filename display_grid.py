import pygame as pg
import rows

def make_window():
    pg.init()
    #create display window
    size = (700,700)
    screen = pg.display.set_mode(size)
    # Set title to the window
    pg.display.set_caption("minesweaper")
    #displays background image
    background_image = pg.image.load("bg.png").convert()
    background_image = pg.transform.rotozoom(background_image, 0, 2)
    screen.blit(background_image, [0, 0])
    pg.display.flip()
    return screen

def new_game_grid(grid , screen):
     
    def display_bombs(np_list,row,y,x):
        n = 0
        #displays the bombs on the grid
        bomb = pg.image.load("hex_bomb.png")
        
        for i in range(9):
            #displays the bombs on the grid
            if np_list[n] >= 50:
                h9 = row[n]
                cord9 = h9.split(",")
                h = int(cord9[0])
                y = int(cord9[1])
                h = h - x
                h = h + 12
                y = y + 8
                screen.blit(bomb, [h,y])

            elif np_list[n]> 0:
                img = "num/num_"+ str(np_list[n]) + ".png"
                n1 = pg.image.load(img)
                h9 = row[n]
                cord9 = h9.split(",")
                h = int(cord9[0])
                y = int(cord9[1])
                h = h - x
                h = h + 12
                y = y + 1
                screen.blit(n1, [h, y])
                

            n = n + 1
        

        
        
    def display_row(row,x,y,grid,gy):
        #dispalys each row
        n = 0
        if row == None:
            row = row(y)
        h1 = row[0]
        h2 = row[1]
        h3 = row[2]
        h4 = row[3]
        h5 = row[4]
        h6 = row[5]
        h7 = row[6]
        h8 = row[7]
        h9 = row[8]


        #splits the list into x and y
        hex = pg.image.load("hex.png")
        cord1 = h1.split(",")
        x1 = int(cord1[0])-x
        y1 = int(cord1[1])
        
        cord2 = h2.split(",")
        x2 = int(cord2[0])-x
        y2 = int(cord2[1])
        
        cord3 = h3.split(",")
        x3 = int(cord3[0])-x
        y3 = int(cord3[1])
        
        cord4 = h4.split(",")
        x4 = int(cord4[0])-x
        y4 = int(cord4[1])
        
        cord5 = h5.split(",")
        x5 = int(cord5[0])-x
        y5 = int(cord5[1])
    
        cord6 = h6.split(",")
        x6 = int(cord6[0])-x
        y6 = int(cord6[1])
    
        cord1 = h6.split(",")
        x6 = int(cord6[0])-x
        y6 = int(cord6[1])
    
        cord7 = h7.split(",")
        x7 = int(cord7[0])-x
        y7 = int(cord7[1])
    
        cord8 = h8.split(",")
        x8 = int(cord8[0])-x
        y8 = int(cord8[1])
    
        cord9 = h9.split(",")
        x9 = int(cord9[0])-x
        y9 = int(cord9[1])

        #displays the tile on screen
        screen.blit(hex, [x1, y1])
        screen.blit(hex, [x2, y2])   
        screen.blit(hex, [x3, y3])
        screen.blit(hex, [x4, y4])
        screen.blit(hex, [x5, y5])
        screen.blit(hex, [x6, y6])
        screen.blit(hex, [x7, y7])   
        screen.blit(hex, [x8, y8])
        screen.blit(hex, [x9, y9])
        #pg.display.update()

    def list_row(grid,y):
        #creates the cords for a row
        #it goes across
        row = []
        x = 0
        for i in range (9):
            n = grid[x,y]   
            row.append(n)
            x = x + 1
        return row


                    
    #list the corddantes for each row
    row_1 = rows.row(159)
    row_2 = rows.row(209)
    row_3 = rows.row(259)
    row_4 = rows.row(309)
    row_5 = rows.row(359)
    row_6 = rows.row(409)
    row_7 = rows.row(459)
    row_8 = rows.row(509)
    row_9= rows.row(559)

    cords = row_1 + row_2 + row_3 + row_4 + row_5 + row_6 + row_7 + row_8 + row_9
    
    #displays ech row
    display_row(row_1,0,121,grid,0)
    display_row(row_2,25,191,grid,1)
    display_row(row_3,0,270,grid,2)
    display_row(row_4,25,300,grid,3)
    display_row(row_5,0,360,grid,4)
    display_row(row_6,25,420,grid,5)
    display_row(row_7,0,480,grid,6)
    display_row(row_8,25,540,grid,7)
    display_row(row_9,0,602,grid,8)

    #list the rows (finds out if there are bombs or numbers)
    row_np_list1 = list_row(grid,0)
    row_np_list2 = list_row(grid,1)
    row_np_list3 = list_row(grid,2)
    row_np_list4 = list_row(grid,3)
    row_np_list5 = list_row(grid,4)
    row_np_list6 = list_row(grid,5)
    row_np_list7 = list_row(grid,6)
    row_np_list8 = list_row(grid,7)
    row_np_list9 = list_row(grid,8)

    #displays the bombs and numbers
    display_bombs(row_np_list1,row_1,85,0)
    display_bombs(row_np_list2,row_2,165,25)
    display_bombs(row_np_list3,row_3,245,0)
    display_bombs(row_np_list4,row_4,325,25)
    display_bombs(row_np_list5,row_5,405,0)
    display_bombs(row_np_list6,row_6,535,25)
    display_bombs(row_np_list7,row_7,625,0)
    display_bombs(row_np_list8,row_8,715,25)
    display_bombs(row_np_list9,row_9,805,0)

    return cords
