import random

import pygame

border=pygame.rect.Rect([10,10,20,20])
bomb=pygame.rect.Rect([400,300,50,50])

speedx=3
speedy=5
side=0
lives=5
lvl=0
bump=10

def model():
    global speedx,speedy,lives,bump,lvl
    bomb.right+=speedx
    bomb.bottom += speedy
    if bomb.right>border.left and side=='right':
        speedx=-speedx
        check()
    if bomb.right>1000:
        speedx =-speedx
        lives-=1
        check()
    if bomb.left < border.right and side=='left':
        speedx =speedx
        check()
    if bomb.left <= 0:
        speedx =speedx
        lives -= 1
        check()
    if bomb.bottom>border.top and side=='down':
        speedy =-speedy
        check()
    if bomb.bottom >= 1000:
        speedy =-speedy
        lives -= 1
        check()
    if bomb.top<border.bottom and side=='up':
        speedy =speedy
        check()
    if bomb.top <= 0:
        speedy =speedy
        lives -= 1
        check()

def check():
    global bump,lives,lvl,speedx,speedy
    bump -= 1
    if bump<=0:
        bump=10
        lvl+=1
        speed=random.choice([1,2])
        if speed==1:
            speedx+=1
        if speed==2:
            speedy+=1


def left():
    global side
    border.x=0
    border.y = 0
    border.w = 100
    border.h = 1000
    side='left'

def right():
    global side
    border.x = 900
    border.y = 0
    border.w = 100
    border.h = 1000
    side='right'
def up():
    global side
    border.x = 0
    border.y = 0
    border.w = 1000
    border.h = 100
    side = 'up'
def down():
    global side
    border.x = 0
    border.y = 900
    border.w = 1000
    border.h = 100
    side = 'down'