import pygame
import model
pygame.init()

screen=pygame.display.set_mode([1000,1000])
font=pygame.font.SysFont('microsofttaile',30)
print(pygame.font.get_fonts())
def view():
    screen.fill([0,0,0])
    pygame.draw.rect(screen,[0,0,255],model.border)
    pygame.draw.rect(screen,[0,255,0],model.bomb)
    text=font.render('lives = '+str(model.lives),True,[255,0,0])
    screen.blit(text,[850,100])
    bumb_text = font.render('bumps = ' + str(model.bump), True, [255, 0, 0])
    screen.blit(bumb_text, [850, 135])
    lvl_text = font.render('lvl = ' + str(model.lvl), True, [255, 0, 0])
    screen.blit(lvl_text, [850, 170])
    pygame.display.flip()