import pygame
pygame.init()
size= width, height= 700,600
white=(255,255,255)
screen = pygame.display.set_mode(size)
radius=25
diameter=50
color=(255,0,0)
xyxy=20
x, y = 25,25
clock = pygame.time.Clock()
FPS = 200
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    keys=pygame.key.get_pressed()
    if keys[pygame.K_UP] and y-radius>= 0:
        y-= xyxy
    if keys[pygame.K_DOWN] and y+radius <=height:
        y+= xyxy
    if keys[pygame.K_LEFT] and x-radius>= 0:
        x-=xyxy
    if keys[pygame.K_RIGHT] and x+radius<= width:
        x+=xyxy
        
    screen.fill(white)
    pygame.draw.circle(screen, color, (x, y), radius)
    pygame.display.update()
    
    clock.tick(FPS)