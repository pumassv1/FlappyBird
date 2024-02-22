import src.Consts as Consts
import pygame
import src.Sounds as Sounds

class Score:
    def __init__(self):
        self.score = 0
        self.game_font = pygame.font.Font('assets/04B_19.TTF',50)

    def show_score(self):
        score_surface = self.game_font.render(str(int(self.score)), True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(288, 50))
        Consts.screen.blit(score_surface, score_rect)

    def update_score(self, pipelist):
        if len(pipelist) <= 2:
            self.score = 0
        else:
            Sounds.Sounds().score()
            self.score += 1