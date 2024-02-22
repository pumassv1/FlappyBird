import src.Consts as Consts
import pygame
import random

class Pipes:
    def __init__(self):
        self.pipe_height = [400,600,800]
        self.pipe_list = []
        self.pipe_surface = pygame.image.load('assets/pipe-green.png')
        self.pipe_surface = pygame.transform.scale2x(self.pipe_surface)

    def create_pipe(self):
        pipe_pos = random.choice(self.pipe_height)
        bottom_pipe = self.pipe_surface.get_rect(midtop=(700, pipe_pos))
        top_pipe = self.pipe_surface.get_rect(midbottom=(700, pipe_pos - 300))
        self.pipe_list.append(bottom_pipe)
        self.pipe_list.append(top_pipe)

    def spawn_pipes(self):
        for pipe in self.pipe_list:
            if pipe.bottom >= 1024:
                Consts.screen.blit(self.pipe_surface, pipe)
            else:
                flip_pipe = pygame.transform.flip(self.pipe_surface,False,True)
                Consts.screen.blit(flip_pipe, pipe)

    def move(self):
        for pipe in self.pipe_list:
            pipe.centerx -= 5

    def remove_pipes(self):
        for pipe in self.pipe_list:
            if pipe.centerx <= -50:
                self.pipe_list.remove(pipe)