import pygame, sys, game


pygame.init()

width = 320
height = 240
screen = pygame.display.set_mode()
entities = []
score = 0

black = 0,0,0

clock = pygame.time.Clock()



def init_game():

    #p = player.player();
    #entities.append(p);
    pass

g = game.game()
player = g.get_player()
player_entity = player.currently_controlled.entity
player_rect = player_entity.get_rect()

# i think in this loop i will mostly handle the drawing and framerate?
# also will handle inputs of course


while(1):
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == ord("w"):
                player.move_around("w") 
        if event.type == pygame.KEYUP:
            if event.key == ord("w"):
                pass

        g.update()

    player_entity = player.currently_controlled.entity
    player_rect = player_entity.get_rect()
    screen.fill(black)
    screen.blit(player_entity, player_rect)
    pygame.display.flip()

    clock.tick(30)






