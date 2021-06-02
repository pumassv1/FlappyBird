import pygame

class Sounds:
    def __init__(self):
        self.death_sound = pygame.mixer.Sound('sound/sfx_die.wav')
        self.score_sound = pygame.mixer.Sound('sound/sfx_point.wav')
        self.wing_sound = pygame.mixer.Sound('sound/sfx_wing.wav')
        self.theme_music = pygame.mixer.Sound('sound/thememusic.wav')

    def wing(self):
        self.wing_sound.play()

    def score(self):
        self.score_sound.play()

    def death(self):
        self.death_sound.play()

    def theme(self):
        self.theme_music.play()
