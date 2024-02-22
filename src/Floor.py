import src.Consts as Consts
import pygame

class Floor:
    def __init__(self):
        self.floor_surface = pygame.image.load('assets/base.png').convert()
        self.floor_surface = pygame.transform.scale2x(self.floor_surface)
        self.floor_surface2 = pygame.image.load('assets/base.png').convert()
        self.floor_surface2 = pygame.transform.scale2x(self.floor_surface2)
        self.floor_x_pos = 0

    def move(self):
        self.floor_x_pos -= 2
        Consts.screen.blit(self.floor_surface, (self.floor_x_pos, 924))
        Consts.screen.blit(self.floor_surface2, (self.floor_x_pos + 576,924))
        if self.floor_x_pos <= -576:
            self.floor_x_pos = 0