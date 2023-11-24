import pygame
import sys
import math
from datetime import datetime
pygame.init()

width, height=829, 826
center=(414, 413)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('mickey mouse')
pygame.display.set_icon(pygame.image.load("mickeyclock.png"))

clockbc = pygame.image.load('main-clock.png' )
left = pygame.image.load('left-hand.png')
right = pygame.image.load('right-hand.png')
image_rect = clockbc.get_rect()
image_rect_r = right.get_rect()
image_rect_l = left.get_rect()

clock = pygame.time.Clock()
FPS = 20000

def chasiki():
    currenttime = datetime.now()
    sec = currenttime.second
    minute = currenttime.minute
    secd= (sec%60)*6-90
    mind=(minute%60)*6-90
    h_rot = pygame.transform.rotate(left, -secd)
    m_rot = pygame.transform.rotate(right, -mind)


    h_rect = h_rot.get_rect(center=center)
    m_rect = m_rot.get_rect(center=center)

    
    screen.blit(h_rot, h_rect)
    screen.blit(m_rot, m_rect)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            

    screen.fill((255, 255, 255))
    screen.blit(clockbc, image_rect)
    chasiki()
    pygame.display.update()
    clock.tick(FPS)
