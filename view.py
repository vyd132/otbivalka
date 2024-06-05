import pygame
import model

screen=pygame.display.set_mode([1000,1000])

def view():
    screen.fill([0,0,0])
    pygame.draw.rect(screen,[0,0,255],model.border)
    pygame.draw.rect(screen,[0,255,0],model.bomb)
    pygame.display.flip()