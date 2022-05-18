import pygame as pg

def display_buttons(empty_grid,screen):

    clicked = False
    #loads the graphic for button
    hex_button = pg.image.load('hex_button.png')

    #creates the groups for the rows (x axis)
    row0 = pg.sprite.Group()
    row1 = pg.sprite.Group()
    row2 = pg.sprite.Group()
    row3 =pg.sprite.Group()
    row4 = pg.sprite.Group()
    row5 = pg.sprite.Group()
    row6 = pg.sprite.Group()
    row7 = pg.sprite.Group()
    row8 = pg.sprite.Group()

    #creates the groups for the columns (y axis)
    column0 = pg.sprite.Group()
    column1 = pg.sprite.Group()
    column2 = pg.sprite.Group()
    column3 =pg.sprite.Group()
    column4 = pg.sprite.Group()
    column5 = pg.sprite.Group()
    column6 = pg.sprite.Group()
    column7 = pg.sprite.Group()
    column8 = pg.sprite.Group()
    
    #create button subclass of sprites
    class Button_Hex(pg.sprite.Sprite):
        def __init__(self,pos, image):
            super().__init__()
            #gets image
            self.image = image
            #gets the dimentions of the imgage
            self.rect = self.image.get_rect()#only wors for rectangles
            #gets the img placement
            self.rect.center = pos


    

    #creates the object
    button1 = Button_Hex((120,200), hex_button)
    #if the button is true it adds button to its corrisonding groups
    if empty_grid[0,0] == 1:
        row0.add(button1)
        column0.add(button1)
    if empty_grid[0,0] == 0:
        pg.sprite.Sprite.kill(button1)

    button2 = Button_Hex((175,200), hex_button)
    if empty_grid[1,0] == 1:
        row1.add(button2)
        column0.add(button2)
    if empty_grid[1,0] == 0:
        pg.sprite.Sprite.kill(button2)

    button3 = Button_Hex((230,200), hex_button)
    if empty_grid[2,0] == 1:
        row2.add(button3)
        column0.add(button3)
    if empty_grid[2,0] == 0:
        pg.sprite.Sprite.kill(button3)

    button4 = Button_Hex((285,200), hex_button)
    if empty_grid[3,0] == 1:
        row3.add(button4)
        column0.add(button4)
    if empty_grid[3,0] == 0:
        pg.sprite.Sprite.kill(button4)

    button5 = Button_Hex((340,200), hex_button)
    if empty_grid[4,0] == 1:
        row4.add(button5)
        column0.add(button5)
    if empty_grid[4,0] == 0:
        pg.sprite.Sprite.kill(button5)

    button6 = Button_Hex((395,200), hex_button)
    if empty_grid[5,0] == 1:
        row5.add(button6)
        column0.add(button6)
    if empty_grid[5,0] == 0:
        pg.sprite.Sprite.kill(button6)

    button7 = Button_Hex((450,200), hex_button)
    if empty_grid[6,0] == 1:
        row6.add(button7)
        column0.add(button7)
    if empty_grid[6,0] == 0:
        pg.sprite.Sprite.kill(button7)

    button8 = Button_Hex((505,200), hex_button)
    if empty_grid[7,0] == 1:
        row7.add(button8)
        column0.add(button8)
    if empty_grid[7,0] == 0:
        pg.sprite.Sprite.kill(button8)

    button9 = Button_Hex((560,200), hex_button)
    if empty_grid[8,0] == 1:
        row8.add(button9)
        column0.add(button9)
    if empty_grid[8,0] == 0:
        pg.sprite.Sprite.kill(button9)

    button10 = Button_Hex((95,250), hex_button)
    if empty_grid[0,1] == 1:
        row0.add(button10)
        column1.add(button10)
    if empty_grid[0,1] == 0:
        pg.sprite.Sprite.kill(button10)

    button11 = Button_Hex((150,250), hex_button)
    if empty_grid[1,1] == 1:
        row1.add(button11)
        column1.add(button11)
    if empty_grid[1,1] == 0:
        pg.sprite.Sprite.kill(button11)

    button12 = Button_Hex((205,250), hex_button)
    if empty_grid[2,1] == 1:
        row2.add(button12)
        column1.add(button12)
    if empty_grid[2,1] == 0:
        pg.sprite.Sprite.kill(button12)

    button13 = Button_Hex((260,250), hex_button)
    if empty_grid[3,1] == 1:
        row3.add(button13)
        column1.add(button13)
    if empty_grid[3,1] == 0:
        pg.sprite.Sprite.kill(button13)

    button14 = Button_Hex((315,250), hex_button)
    if empty_grid[4,1] == 1:
        row4.add(button14)
        column1.add(button14)
    if empty_grid[4,1] == 0:
        pg.sprite.Sprite.kill(button14)

    button15 = Button_Hex((370,250), hex_button)
    if empty_grid[5,1] == 1:
        row5.add(button15)
        column1.add(button15)
    if empty_grid[5,1] == 0:
        pg.sprite.Sprite.kill(button15)

    button16 = Button_Hex((425,250), hex_button)
    if empty_grid[6,1] == 1:
        row6.add(button16)
        column1.add(button16)
    if empty_grid[6,1] == 0:
        pg.sprite.Sprite.kill(button16)

    button17 = Button_Hex((480,250), hex_button)
    if empty_grid[7,1] == 1:
        row7.add(button17)
        column1.add(button17)
    if empty_grid[7,1] == 0:
        pg.sprite.Sprite.kill(button17)

    button18 = Button_Hex((535,250), hex_button)
    if empty_grid[8,1] == 1:
        row8.add(button18)
        column1.add(button18)
    if empty_grid[8,1] == 0:
        pg.sprite.Sprite.kill(button18)

    button19 = Button_Hex((120,300), hex_button)
    if empty_grid[0,2] == 1:
        row0.add(button19)
        column2.add(button19)
    if empty_grid[0,2] == 0:
        pg.sprite.Sprite.kill(button19)

    button20 = Button_Hex((175,300), hex_button)
    if empty_grid[1,2] == 1:
        row1.add(button20)
        column2.add(button20)
    if empty_grid[1,2] == 0:
        pg.sprite.Sprite.kill(button20)

    button21 = Button_Hex((230,300), hex_button)
    if empty_grid[2,2] == 1:
        row2.add(button21)
        column2.add(button21)
    if empty_grid[2,2] == 0:
        pg.sprite.Sprite.kill(button21)

    button22 = Button_Hex((285,300), hex_button)
    if empty_grid[3,2] == 1:
        row3.add(button22)
        column2.add(button22)
    if empty_grid[3,2] == 0:
        pg.sprite.Sprite.kill(button22)

    button23 = Button_Hex((340,300), hex_button)
    if empty_grid[4,2] == 1:
        row4.add(button23)
        column2.add(button23)
    if empty_grid[4,2] == 0:
        pg.sprite.Sprite.kill(button23)

    button24 = Button_Hex((395,300), hex_button)
    if empty_grid[5,2] == 1:
        row5.add(button24)
        column2.add(button24)
    if empty_grid[5,2] == 0:
        pg.sprite.Sprite.kill(button24)

    button25 = Button_Hex((450,300), hex_button)
    if empty_grid[6,2] == 1:
        row6.add(button25)
        column2.add(button25)
    if empty_grid[6,2] == 0:
        pg.sprite.Sprite.kill(button25)

    button26 = Button_Hex((505,300), hex_button)
    if empty_grid[7,2] == 1:
        row7.add(button26)
        column2.add(button26)
    if empty_grid[7,2] == 0:
        pg.sprite.Sprite.kill(button26)

    button27 = Button_Hex((560,300), hex_button)
    if empty_grid[8,2] == 1:
        row8.add(button27)
        column2.add(button27)
    if empty_grid[8,2] == 0:
        pg.sprite.Sprite.kill(button27)

    button28 = Button_Hex((95,350), hex_button)
    if empty_grid[0,3] == 1:
        row0.add(button28)
        column3.add(button28)
    if empty_grid[0,3] == 0:
        pg.sprite.Sprite.kill(button28)

    button29 = Button_Hex((150,350), hex_button)
    if empty_grid[1,3] == 1:
        row1.add(button29)
        column3.add(button29)
    if empty_grid[1,3] == 0:
        pg.sprite.Sprite.kill(button29)

    button30 = Button_Hex((205,350), hex_button)
    if empty_grid[2,3] == 1:
        row2.add(button30)
        column3.add(button30)
    if empty_grid[2,3] == 0:
        pg.sprite.Sprite.kill(button30)

    button31 = Button_Hex((260,350), hex_button)
    if empty_grid[3,3] == 1:
        row3.add(button31)
        column3.add(button31)
    if empty_grid[3,3] == 0:
        pg.sprite.Sprite.kill(button31)

    button32 = Button_Hex((315,350), hex_button)
    if empty_grid[4,3] == 1:
        row4.add(button32)
        column3.add(button32)
    if empty_grid[4,3] == 0:
        pg.sprite.Sprite.kill(button32)

    button33 = Button_Hex((370,350), hex_button)
    if empty_grid[5,3] == 1:
        row5.add(button33)
        column3.add(button33)
    if empty_grid[5,3] == 0:
        pg.sprite.Sprite.kill(button33)

    button34 = Button_Hex((425,350), hex_button)
    if empty_grid[6,3] == 1:
        row6.add(button34)
        column3.add(button34)
    if empty_grid[6,3] == 0:
        pg.sprite.Sprite.kill(button34)

    button35 = Button_Hex((480,350), hex_button)
    if empty_grid[7,3] == 1:
        row7.add(button35)
        column3.add(button35)
    if empty_grid[7,3] == 0:
        pg.sprite.Sprite.kill(button35)

    button36 = Button_Hex((535,350), hex_button)
    if empty_grid[8,3] == 1:
        row8.add(button36)
        column3.add(button36)
    if empty_grid[8,3] == 0:
        pg.sprite.Sprite.kill(button36)

    button37 = Button_Hex((120,400), hex_button)
    if empty_grid[0,4] == 1:
        row0.add(button37)
        column4.add(button37)
    if empty_grid[0,4] == 0:
        pg.sprite.Sprite.kill(button37)

    button38 = Button_Hex((175,400), hex_button)
    if empty_grid[1,4] == 1:
        row1.add(button38)
        column4.add(button38)
    if empty_grid[1,4] == 0:
        pg.sprite.Sprite.kill(button38)

    button39 = Button_Hex((230,400), hex_button)
    if empty_grid[2,4] == 1:
        row2.add(button39)
        column4.add(button39)
    if empty_grid[2,4] == 0:
        pg.sprite.Sprite.kill(button39)

    button40 = Button_Hex((285,400), hex_button)
    if empty_grid[3,4] == 1:
        row3.add(button40)
        column4.add(button40)
    if empty_grid[3,4] == 0:
        pg.sprite.Sprite.kill(button40)

    button41 = Button_Hex((340,400), hex_button)
    if empty_grid[4,4] == 1:
        row4.add(button41)
        column4.add(button41)
    if empty_grid[4,4] == 0:
        pg.sprite.Sprite.kill(button41)

    button42 = Button_Hex((395,400), hex_button)
    if empty_grid[5,4] == 1:
        row5.add(button42)
        column4.add(button42)
    if empty_grid[5,4] == 0:
        pg.sprite.Sprite.kill(button42)

    button43 = Button_Hex((450,400), hex_button)
    if empty_grid[6,4] == 1:
        row6.add(button43)
        column4.add(button43)
    if empty_grid[6,4] == 0:
        pg.sprite.Sprite.kill(button43)

    button44 = Button_Hex((505,400), hex_button)
    if empty_grid[7,4] == 1:
        row7.add(button44)
        column4.add(button44)
    if empty_grid[7,4] == 0:
        pg.sprite.Sprite.kill(button44)

    button45 = Button_Hex((560,400), hex_button)
    if empty_grid[8,4] == 1:
        row8.add(button45)
        column4.add(button45)
    if empty_grid[8,4] == 0:
        pg.sprite.Sprite.kill(button45)

    button46 = Button_Hex((95,450), hex_button)
    if empty_grid[0,5] == 1:
        row0.add(button46)
        column5.add(button46)
    if empty_grid[0,5] == 0:
        pg.sprite.Sprite.kill(button46)

    button47 = Button_Hex((150,450), hex_button)
    if empty_grid[1,5] == 1:
        row1.add(button47)
        column5.add(button47)
    if empty_grid[1,5] == 0:
        pg.sprite.Sprite.kill(button47)

    button48 = Button_Hex((205,450), hex_button)
    if empty_grid[2,5] == 1:
        row2.add(button48)
        column5.add(button48)
    if empty_grid[2,5] == 0:
        pg.sprite.Sprite.kill(button48)

    button49 = Button_Hex((260,450), hex_button)
    if empty_grid[3,5] == 1:
        row3.add(button49)
        column5.add(button49)
    if empty_grid[3,5] == 0:
        pg.sprite.Sprite.kill(button49)

    button50 = Button_Hex((315,450), hex_button)
    if empty_grid[4,5] == 1:
        row4.add(button50)
        column5.add(button50)
    if empty_grid[4,5] == 0:
        pg.sprite.Sprite.kill(button50)

    button51 = Button_Hex((370,450), hex_button)
    if empty_grid[5,5] == 1:
        row5.add(button51)
        column5.add(button51)
    if empty_grid[5,5] == 0:
        pg.sprite.Sprite.kill(button51)

    button52 = Button_Hex((425,450), hex_button)
    if empty_grid[6,5] == 1:
        row6.add(button52)
        column5.add(button52)
    if empty_grid[6,5] == 0:
        pg.sprite.Sprite.kill(button52)

    button53 = Button_Hex((480,450), hex_button)
    if empty_grid[7,5] == 1:
        row7.add(button53)
        column5.add(button53)
    if empty_grid[7,5] == 0:
        pg.sprite.Sprite.kill(button53)

    button54 = Button_Hex((535,450), hex_button)
    if empty_grid[8,5] == 1:
        row8.add(button54)
        column5.add(button54)
    if empty_grid[8,5] == 0:
        pg.sprite.Sprite.kill(button54)

    button55 = Button_Hex((120,500), hex_button)
    if empty_grid[0,6] == 1:
        row0.add(button55)
        column6.add(button55)
    if empty_grid[0,6] == 0:
        pg.sprite.Sprite.kill(button55)

    button56 = Button_Hex((175,500), hex_button)
    if empty_grid[1,6] == 1:
        row1.add(button56)
        column6.add(button56)
    if empty_grid[1,6] == 0:
        pg.sprite.Sprite.kill(button56)

    button57 = Button_Hex((230,500), hex_button)
    if empty_grid[2,6] == 1:
        row2.add(button57)
        column6.add(button57)
    if empty_grid[2,6] == 0:
        pg.sprite.Sprite.kill(button57)

    button58 = Button_Hex((285,500), hex_button)
    if empty_grid[3,6] == 1:
        row3.add(button58)
        column6.add(button58)
    if empty_grid[3,6] == 0:
        pg.sprite.Sprite.kill(button58)

    button59 = Button_Hex((340,500), hex_button)
    if empty_grid[4,6] == 1:
        row4.add(button59)
        column6.add(button59)
    if empty_grid[4,6] == 0:
        pg.sprite.Sprite.kill(button59)

    button60 = Button_Hex((395,500), hex_button)
    if empty_grid[5,6] == 1:
        row5.add(button60)
        column6.add(button60)
    if empty_grid[5,6] == 0:
        pg.sprite.Sprite.kill(button60)

    button61 = Button_Hex((450,500), hex_button)
    if empty_grid[6,6] == 1:
        row6.add(button61)
        column6.add(button61)
    if empty_grid[6,6] == 0:
        pg.sprite.Sprite.kill(button61)

    button62 = Button_Hex((505,500), hex_button)
    if empty_grid[7,6] == 1:
        row7.add(button62)
        column6.add(button62)
    if empty_grid[7,6] == 0:
        pg.sprite.Sprite.kill(button62)

    button63 = Button_Hex((560,500), hex_button)
    if empty_grid[8,6] == 1:
        row8.add(button63)
        column6.add(button63)
    if empty_grid[8,6] == 0:
        pg.sprite.Sprite.kill(button63)

    button64 = Button_Hex((95,550), hex_button)
    if empty_grid[0,7] == 1:
        row0.add(button64)
        column7.add(button64)
    if empty_grid[0,7] == 0:
        pg.sprite.Sprite.kill(button64)

    button65 = Button_Hex((150,550), hex_button)
    if empty_grid[1,7] == 1:
        row1.add(button65)
        column7.add(button65)
    if empty_grid[1,7] == 0:
        pg.sprite.Sprite.kill(button65)

    button66 = Button_Hex((205,550), hex_button)
    if empty_grid[2,7] == 1:
        row2.add(button66)
        column7.add(button66)
    if empty_grid[2,7] == 0:
        pg.sprite.Sprite.kill(button66)

    button67 = Button_Hex((260,550), hex_button)
    if empty_grid[3,7] == 1:
        row3.add(button67)
        column7.add(button67)
    if empty_grid[3,7] == 0:
        pg.sprite.Sprite.kill(button67)

    button68 = Button_Hex((315,550), hex_button)
    if empty_grid[4,7] == 1:
        row4.add(button68)
        column7.add(button68)
    if empty_grid[4,7] == 0:
        pg.sprite.Sprite.kill(button68)

    button69 = Button_Hex((370,550), hex_button)
    if empty_grid[5,7] == 1:
        row5.add(button69)
        column7.add(button69)
    if empty_grid[5,7] == 0:
        pg.sprite.Sprite.kill(button69)

    button70 = Button_Hex((425,550), hex_button)
    if empty_grid[6,7] == 1:
        row6.add(button70)
        column7.add(button70)
    if empty_grid[6,7] == 0:
        pg.sprite.Sprite.kill(button70)

    button71 = Button_Hex((480,550), hex_button)
    if empty_grid[7,7] == 1:
        row7.add(button71)
        column7.add(button71)
    if empty_grid[7,7] == 0:
        pg.sprite.Sprite.kill(button71)

    button72 = Button_Hex((535,550), hex_button)
    if empty_grid[8,7] == 1:
        row8.add(button72)
        column7.add(button72)
    if empty_grid[8,7] == 0:
        pg.sprite.Sprite.kill(button72)

    button73 = Button_Hex((120,600), hex_button)
    if empty_grid[0,8] == 1:
        row0.add(button73)
        column8.add(button73)
    if empty_grid[0,8] == 0:
        pg.sprite.Sprite.kill(button73)

    button74 = Button_Hex((175,600), hex_button)
    if empty_grid[1,8] == 1:
        row1.add(button74)
        column8.add(button74)
    if empty_grid[1,8] == 0:
        pg.sprite.Sprite.kill(button74)

    button75 = Button_Hex((230,600), hex_button)
    if empty_grid[2,8] == 1:
        row2.add(button75)
        column8.add(button75)
    if empty_grid[2,8] == 0:
        pg.sprite.Sprite.kill(button75)

    button76 = Button_Hex((285,600), hex_button)
    if empty_grid[3,8] == 1:
        row3.add(button76)
        column8.add(button76)
    if empty_grid[3,8] == 0:
        pg.sprite.Sprite.kill(button76)

    button77 = Button_Hex((340,600), hex_button)
    if empty_grid[4,8] == 1:
        row4.add(button77)
        column8.add(button77)
    if empty_grid[4,8] == 0:
        pg.sprite.Sprite.kill(button77)

    button78 = Button_Hex((395,600), hex_button)
    if empty_grid[5,8] == 1:
        row5.add(button78)
        column8.add(button78)
    if empty_grid[5,8] == 0:
        pg.sprite.Sprite.kill(button78)

    button79 = Button_Hex((450,600), hex_button)
    if empty_grid[6,8] == 1:
        row6.add(button79)
        column8.add(button79)
    if empty_grid[6,8] == 0:
        pg.sprite.Sprite.kill(button79)

    button80 = Button_Hex((505,600), hex_button)
    if empty_grid[7,8] == 1:
        row7.add(button80)
        column8.add(button80)
    if empty_grid[7,8] == 0:
        pg.sprite.Sprite.kill(button80)

    button81 = Button_Hex((560,600), hex_button)
    if empty_grid[8,8] == 1:
        row8.add(button81)
        column8.add(button81)
    if empty_grid[8,8] == 0:
        pg.sprite.Sprite.kill(button81)

    #sees if the user has clickes
    while clicked == False:
        user_y = 0
        for event in pg.event.get():
            #if user clicks it sees if it clicked a button and finds out hte x and y posioning on grid og the button.
            if event.type == pg.MOUSEBUTTONDOWN:
                pos = pg.mouse.get_pos()

                x = int(pos[0])
                y = int(pos[1])

                clicked_sprites = [sprite for sprite in row0 if sprite.rect.collidepoint(x, y)]
                for i in clicked_sprites:
                    user_x = 0
                    clicked = True
                    
                clicked_sprites = [sprite for sprite in row1 if sprite.rect.collidepoint(x, y)]
                for i in clicked_sprites:
                    user_x = 1
                    clicked = True

                clicked_sprites = [sprite for sprite in row2 if sprite.rect.collidepoint(x, y)]
                for i in clicked_sprites:
                    user_x = 2
                    clicked = True

                clicked_sprites = [sprite for sprite in row3 if sprite.rect.collidepoint(x, y)]
                for i in clicked_sprites:
                    user_x = 3
                    clicked = True

                clicked_sprites = [sprite for sprite in row4 if sprite.rect.collidepoint(x, y)]
                for i in clicked_sprites:
                    user_x = 4
                    clicked = True

                clicked_sprites = [sprite for sprite in row5 if sprite.rect.collidepoint(x, y)]
                for i in clicked_sprites:
                    user_x = 5
                    clicked = True

                clicked_sprites = [sprite for sprite in row6 if sprite.rect.collidepoint(x, y)]
                for i in clicked_sprites:
                    user_x = 6
                    clicked = True

                clicked_sprites = [sprite for sprite in row7 if sprite.rect.collidepoint(x, y)]
                for i in clicked_sprites:
                    user_x = 7
                    clicked = True
                    
                clicked_sprites = [sprite for sprite in row8 if sprite.rect.collidepoint(x, y)]
                for i in clicked_sprites:
                    user_x = 8
                    clicked = True

                    clicked_sprites = [sprite for sprite in column0 if sprite.rect.collidepoint(x, y)]
                for i in clicked_sprites:
                    user_y = 0
                    clicked = True
                    
                clicked_sprites = [sprite for sprite in column1 if sprite.rect.collidepoint(x, y)]
                for i in clicked_sprites:
                    user_y = 1
                    clicked = True

                clicked_sprites = [sprite for sprite in column2 if sprite.rect.collidepoint(x, y)]
                for i in clicked_sprites:
                    user_y = 2
                    clicked = True

                clicked_sprites = [sprite for sprite in column3 if sprite.rect.collidepoint(x, y)]
                for i in clicked_sprites:
                    user_y = 3
                    clicked = True

                clicked_sprites = [sprite for sprite in column4 if sprite.rect.collidepoint(x, y)]
                for i in clicked_sprites:
                    user_y = 4
                    clicked = True

                clicked_sprites = [sprite for sprite in column5 if sprite.rect.collidepoint(x, y)]
                for i in clicked_sprites:
                    user_y = 5
                    clicked = True

                clicked_sprites = [sprite for sprite in column6 if sprite.rect.collidepoint(x, y)]
                for i in clicked_sprites:
                    user_y = 6
                    clicked = True

                clicked_sprites = [sprite for sprite in column7 if sprite.rect.collidepoint(x, y)]
                for i in clicked_sprites:
                    user_y = 7
                    clicked = True
                    
                clicked_sprites = [sprite for sprite in column8 if sprite.rect.collidepoint(x, y)]
                for i in clicked_sprites:
                    user_y = 8
                    clicked = True


    
        #displays the buttons
        row0.draw(screen)
        row1.draw(screen)
        row2.draw(screen)
        row3.draw(screen)
        row4.draw(screen)
        row5.draw(screen)
        row6.draw(screen)
        row7.draw(screen)
        row8.draw(screen)  
        pg.display.update()

    
    cords = [user_x,user_y]
    #empty the groups
    pg.sprite.Group.empty(row0)
    pg.sprite.Group.empty(row1)
    pg.sprite.Group.empty(row2)
    pg.sprite.Group.empty(row3)
    pg.sprite.Group.empty(row4)
    pg.sprite.Group.empty(row5)
    pg.sprite.Group.empty(row6)
    pg.sprite.Group.empty(row7)
    pg.sprite.Group.empty(row8)

    pg.sprite.Group.empty(column0)
    pg.sprite.Group.empty(column1)
    pg.sprite.Group.empty(column2)
    pg.sprite.Group.empty(column3)
    pg.sprite.Group.empty(column4)
    pg.sprite.Group.empty(column5)
    pg.sprite.Group.empty(column6)
    pg.sprite.Group.empty(column7)
    pg.sprite.Group.empty(column8)

    #returns the button the user clicked
    return cords