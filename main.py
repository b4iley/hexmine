#imports the other files
import game
import display_grid
import button_display
import game_graphics
#imports pygame
import pygame as pg

game_contine = True

#this creates the grid for the game
grid =game.make_grid()
#creates window
screen =display_grid.make_window()
#makes grid to tell if the button on the title is still there
empty_grid = game.make_empty_grid()


while game_contine == True:
        #displays grid on window
        display_grid.new_game_grid(grid,screen)
        #shows the buttons and collects the user input
        cord = button_display.display_buttons(empty_grid,screen)
        #splits the data for the next module so it can be used
        x = cord[0]
        y = cord [1]
        #clears the buttons that the user clciked and anyothers which should be as well
        empty_grid = game.check_grid(x,y,empty_grid,grid,screen)
        #sees if there are any other buttons other than ones covering bombs
        game_contine = game_graphics.win(empty_grid,screen)
