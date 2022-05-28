import pygame, sys, game


pygame.init()

width = 320
height = 240
screen = pygame.display.set_mode()
entities = []
score = 0

black = 0,100,0

clock = pygame.time.Clock()



def init_game():

    #p = player.player();
    #entities.append(p);
    pass

g = game.game()
player = g.player
player_entity = player.currently_controlled.entity
player_rect = player_entity.get_rect()

# i think in this loop i will mostly handle the drawing and framerate?
# also will handle inputs of course


while(1):
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player.move_around("w") 
            if (event.key == pygame.K_s):
                player.move_around("s") 
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                # this code right here will have to be rewritten
                # because the true case is when either were at a bound
                # or wasd arent being held
                player.stop_movement()

        g.update()

    player_entity = player.currently_controlled.entity
    player_rect = player.currently_controlled.entity_rect
    screen.fill(black)
    screen.blit(player_entity, player_rect)
    pygame.display.flip()

    clock.tick(30)






