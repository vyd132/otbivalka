import pygame,model

def event():
    events=pygame.event.get()
    for event in events:
        if event.type==pygame.QUIT:
            exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                model.left()
            if event.key==pygame.K_RIGHT:
                model.right()
            if event.key == pygame.K_UP:
                model.up()
            if event.key == pygame.K_DOWN:
                model.down()



