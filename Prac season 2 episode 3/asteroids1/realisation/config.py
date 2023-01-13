import pygame
from random import choice

sw = 1000  #all bg staff
sh = 800
backgrounds = []
backgrounds.append(pygame.image.load('background1.png'))
backgrounds.append(pygame.image.load('background2.png'))
backgrounds.append(pygame.image.load('background3.png'))
bg = pygame.transform.scale(choice(backgrounds), (sw, sh))

fps = 40  #кадры в секунду
start_lives = 3    #making 3 lives as given
asteroid_spawn_delay = 50 #частота появления астероидов
score_per_hit = 1  #кол-во очков за одно попадание

#cool graphic for explosion
explosions = []
explosions.append(pygame.image.load('expl1.png'))
explosions.append(pygame.image.load('expl2.png'))
explosions.append(pygame.image.load('expl3.png'))
explosions.append(pygame.image.load('expl4.png'))
explosions.append(pygame.image.load('expl5.png'))
explosions.append(pygame.image.load('expl6.png'))
explosions.append(pygame.image.load('expl7.png'))
explosions.append(pygame.image.load('expl8.png'))
explosions.append(pygame.image.load('expl9.png'))
explosions.append(pygame.image.load('expl10.png'))
explosions.append(pygame.image.load('expl11.png'))
explosions.append(pygame.image.load('expl12.png'))

#вылет огня
bullet_distance = 450
rocket_sprite = pygame.image.load('rocket.png')
bullet_h = 10
bullet_w = 10
bullet_max_speed = 15

#player configuration
player_max_speed = 10
player_radial_speed = 7
spaceship_sprite = pygame.image.load('ship.png')
spaceship_sprite = pygame.transform.rotate(spaceship_sprite, 90)

spaceship_move_sprite = pygame.image.load('ship_thrusted.png')
spaceship_move_sprite = pygame.transform.rotate(spaceship_move_sprite, 90)

#asteroids
asteroid1_sprite = pygame.image.load('asteroid1.png')
asteroid2_sprite = pygame.image.load('asteroid2.png')
asteroid3_sprite = pygame.image.load('asteroid3.png')
asteroid_sprites = [asteroid1_sprite, asteroid2_sprite, asteroid3_sprite]

asteroid_min_size = 40
asteroid_max_size = 80
asteroid_max_speed = 2