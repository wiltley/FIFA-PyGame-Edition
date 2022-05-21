import pygame, sys, player


pygame.init()

width = 320
height = 240
screen = pygame.display.set_mode();
entities = [];

def init_game():

    p = player.player();
    entities.append(p);
    pass




# i think in this loop i will mostly handle the drawing and framerate?
while(1):
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()




