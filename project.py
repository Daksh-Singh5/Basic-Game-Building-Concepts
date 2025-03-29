import pygame

pygame.init()
width = 1000
height = 1000
show = pygame.display.set_mode((width,height))

colour = {
    "blue":pygame.Color("blue"),
    "red":pygame.Color("red"),
    "yellow":pygame.Color("yellow"),
    "orange":pygame.Color("orange"),
    "green":pygame.Color("green"),

}              

nowColour=colour["orange"]
X,Y=500,500
boxRadius = 100
boxwidth = 400
    
Fps = pygame.time.Clock()

working=True

while working:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            working = False
    press = pygame.key.get_pressed()
    if press[pygame.K_LEFT]:X-= 3
    if press[pygame.K_RIGHT]:X += 3
    if press[pygame.K_UP]:Y -= 3
    if press[pygame.K_DOWN]:Y += 3

    X = min(max(0,X),width - boxRadius)
    Y = min(max(0,Y),height - boxRadius)

    if X == boxRadius: nowColour = colour["green"]
    elif Y == 0: nowColour = colour["red"]
    elif X == width - boxRadius: nowColour = colour["yellow"]
    elif Y == height - boxRadius: nowColour = colour["blue"]
    else: nowColour = colour["orange"]

    show.fill((0,0,0))
    pygame.draw.circle(show,nowColour,(X,Y),boxRadius,boxwidth)

    pygame.display.flip()
    Fps.tick(90)
pygame.quit()
