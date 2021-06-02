import pygame

class Bird:
    def __init__(self):
        self.bird_surface = pygame.transform.scale2x(pygame.image.load('assets/bluebird-midflap.png').convert_alpha())
        self.bird_surface_down = pygame.transform.scale2x(pygame.image.load('assets/bluebird-downflap.png').convert_alpha())
        self.bird_surface_up = pygame.transform.scale2x(pygame.image.load('assets/bluebird-upflap.png').convert_alpha())
        self.movement = 0
        self.gravity = 0.5
        self.bird_rect = self.bird_surface.get_rect(center=(100,512))

    def move(self):
        self.movement += self.gravity
        self.bird_rect.centery += self.movement

    def moveup(self):
        self.movement = 0
        self.movement = -12
        self.bird_rect.centery += self.movement

    def animation(self):
        if self.movement == 0:
            return pygame.transform.rotozoom(self.bird_surface, -self.movement * 1.5, 1)
        elif self.movement > 0:
            return pygame.transform.rotozoom(self.bird_surface_up, -self.movement * 1.5, 1)
        else:
            return pygame.transform.rotozoom(self.bird_surface_down, -self.movement * 1.5, 1)




