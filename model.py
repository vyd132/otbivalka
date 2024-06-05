import pygame

border=pygame.rect.Rect([10,10,20,20])
bomb=pygame.rect.Rect([400,300,50,50])

speedx=3
speedy=5

def model():
    global speedx,speedy
    bomb.right+=speedx
    bomb.bottom += speedy
    if bomb.right>=border.left:
        speedx = -3
    if bomb.right>=1000:
        speedx=-3
    if bomb.left <= 0:
        speedx = 3
    if bomb.bottom >= 1000:
        speedy=-5
    if bomb.top <= 0:
        speedy=5


def left():
    border.x=0
    border.y = 0
    border.w = 100
    border.h = 1000

def right():
    border.x = 900
    border.y = 0
    border.w = 100
    border.h = 1000

def up():
    border.x = 0
    border.y = 0
    border.w = 1000
    border.h = 100

def down():
    border.x = 0
    border.y = 900
    border.w = 1000
    border.h = 100