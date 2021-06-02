import Consts
import Floor
import Pipes
import Bird
import Score
import Sounds
import CollisionManager
import pygame
import sys


class GameManager:
    def __init__(self):
        pygame.init()
        self.floor = Floor.Floor()
        self.bird = Bird.Bird()
        self.pipe = Pipes.Pipes()
        self.score = Score.Score()
        self.sound = Sounds.Sounds()
        self.game_status = True

    def reset_game(self):
        self.pipe.pipe_list = []
        self.bird.bird_rect.center = (100, 100)
        self.score.score = 0

    def game_loop(self):
        self.sound.theme()
        while True:
            Consts.screen.blit(Consts.bg_surface, (0,0))
            if self.game_status:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.sound.wing()
                            self.bird.moveup()
                    if event.type == Consts.SPAWNPIPE:
                        self.pipe.create_pipe()

                    if event.type == Consts.UPDATESCORE:
                        self.score.update_score(self.pipe.pipe_list)

                Consts.screen.blit(self.bird.animation(), self.bird.bird_rect)
                self.pipe.move()
                self.pipe.spawn_pipes()
                self.pipe.remove_pipes()
                self.floor.move()
                self.bird.move()
                self.score.show_score()


                if CollisionManager.CollisionManager().check_collisions(self.bird.bird_rect, self.pipe.pipe_list):
                    self.sound.death()
                    self.game_status = False

            else:
                Consts.screen.blit(Consts.game_over_screen, (100, 312))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.reset_game()
                            self.game_status = True

            pygame.display.update()
            Consts.clock.tick(60)




