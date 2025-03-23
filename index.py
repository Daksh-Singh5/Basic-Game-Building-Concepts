import pygame

pygame.init()
show = pygame.display.set_mode((1000,1000))
working=True

while working:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            working = False
    pygame.draw.rect(show,(0,0,255),pygame.Rect(150,150,100,100))
    pygame.display.flip()