import numpy as np
import pygame as pg
import replay_game


def menu():
    class Button(pg.sprite.Sprite):
        def __init__(self,pos, image):
            super().__init__()
            #gets image
            self.image = image
            #gets the dimentions of the imgage
            self.rect = self.image.get_rect()#only wors for rectangles
            #gets the img placement
            self.rect.center = pos
    playbttn = pg.image.load("play_bttn.png")
    quitbttn = pg.image.load("quit_bttn.png")
    play_button = Button((220, 220),playbttn)
    play_button.draw()
    replay_game.game_replay()

def win(empty_grid,screen):
    game_contiune = True
    sum_eg = np.sum(empty_grid)
    if sum_eg == 9:
        win_screen = pg.image.load('win_screen.png')
        screen.blit(win_screen, (200,200))
        pg.display.update()
        game_contiune = False
        replay_game.game_replay()

    return game_contiune

def end(screen):
    win_screen = pg.image.load('bomb_screen.png')
    screen.blit(win_screen, (150,180))
    pg.display.update()
    menu()
