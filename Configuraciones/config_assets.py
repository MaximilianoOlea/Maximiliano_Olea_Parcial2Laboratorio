import pygame

#Pantalla
WIDTH = 1800
HEIGHT = 900
SIZE_SCREEN = (WIDTH, HEIGHT)

CENTER_X = WIDTH//2
CENTER_Y = HEIGHT//2
CENTER = (CENTER_X, CENTER_Y)

DISPLAY_LEFT = 0
DISPLAY_RIGHT = WIDTH
DISPLAY_TOP = 0
DISPLAY_BOTTOM = HEIGHT
DISPLAY_MIDTOP = (CENTER_X, DISPLAY_TOP)

SIZE_ICON = (32, 32)
ORIGIN = (0, 0)

FPS = 60
SPEED = 5

#Colores
ROJO = pygame.color.Color(255,0,0)
AZUL = pygame.color.Color(0,0,255)
VERDE = pygame.color.Color(0,255,0)
NEGRO = pygame.color.Color(0,0,0)
BLANCO = pygame.color.Color(255,255,255)
CUSTOM = pygame.color.Color(125,249,243)
AMARILLO = pygame.color.Color(238, 253, 42)

#Pingu (Personaje Principal)
main_character_x = CENTER_X
main_character_y = HEIGHT - 150

SIZE_MAIN_CHARACTER= (50,80)
SPEED_FALL_MAIN_CHARACTER = 8
SPEED_SHOOT_RELOAD = 0.5
SPEED_MAIN_CHARACTER = 7
JUMP_POWER_MAIN_CHARACTER = 20
GRAVITY_MAIN_CHARACTER = 1
COUNT_LIFE_PINGU = 1
#Enemigos:
#bird:

SIZE_ENEMY_BIRD= (120,120)
SPEED_BIRD = 3

#wolf
SIZE_ENEMY_WOLF= (120,70)
SPEED_WOLF = 2

#ghost
SIZE_ENEMY_GHOST= (100,90)
SPEED_GHOST = 3
#Bosses:
SIZE_BOSS = (90,130)
SPEED_BOSS = 10

#Plataformas:
SIZE_PLATFORM_SMALL = (400,30)
SIZE_PLATFORM_MEDIUM = (650,30)
SIZE_PLATFORM_BIG = (1000,30)

#Climas:
SIZE_CLIMATE = SIZE_SCREEN

SPEED_ANIMATION = 12

#Proyectiles:
SIZE_PROJECTILE = (60,60)
SIZE_PROJECTILE_ENEMY = (80,60)
SPEED_PROJECTILE_ENEMY = 6

#ITEMS:
SIZE_ITEM = (60,60)