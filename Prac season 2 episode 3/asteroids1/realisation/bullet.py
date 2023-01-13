import pygame
from config import sw, sh, bullet_distance, rocket_sprite, bullet_h, bullet_w, bullet_max_speed
from math import sqrt


class Bullet(object):
    def __init__(self, player):
        self.image = rocket_sprite 
        self.image = pygame.transform.scale(self.image, (bullet_w, bullet_h))  #making suitable format
        self.point = player.head  #making bullet start point in the rocket
        self.x, self.y = self.point  #coordinats of bullets
        self.w = bullet_w  #width
        self.h = bullet_h  #hight
        self.c = player.cosin 
        self.s = player.sin  
        self.xv = self.c*bullet_max_speed  # Вычисляем скорость движения по x
        self.yv = self.s*bullet_max_speed  # Вычисляем скорость движения по у
        self.spawn_x, self.spawn_y = self.point  # Записываем точку появления снаряда для дальнейшего вычисления дистанции

    def move(self):  #bullet moving
        self.x += self.xv
        self.y -= self.yv

    def draw(self, win):  #bullet отрисовка
        win.blit(self.image, (self.x, self.y))

    def outside(self):  # Провера на вылет за пределы экрана
        if self.x < -50 or self.x > sw or self.y > sh or self.y < -50:  # Если снаряд за пределами экрана
            return True

    def checkdist(self):  # Проверка на максимальную дистанцию полета снаряда
        if sqrt((self.spawn_x - self.x)**2 + (self.spawn_y - self.y)**2) > bullet_distance:
            return True