import pygame
pygame.init()
pygame.mixer.pre_init(frequency = 44100, size = 16, channels = 1, buffer = 256)

screen = pygame.display.set_mode((576,1024))

bg_surface = pygame.image.load('assets/background-day.png').convert()
bg_surface = pygame.transform.scale2x(bg_surface)
game_over_screen = pygame.transform.scale2x(pygame.image.load('assets/message.png').convert_alpha())


clock = pygame.time.Clock()


SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE,1200)

UPDATESCORE = pygame.USEREVENT + 1
pygame.time.set_timer(UPDATESCORE, 1130)





