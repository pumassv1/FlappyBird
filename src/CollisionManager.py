class CollisionManager:
    def check_collisions(self, bird, pipes):
        if bird.centery >= 923 or bird.centery <= 0:
            return True
        for pipe in pipes:
            if bird.colliderect(pipe):
                return True
        return False