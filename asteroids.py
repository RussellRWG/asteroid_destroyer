import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, WHITE
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, self.position, self.radius)

    def update(self, dt):
        self.position = (self.velocity * dt) + self.position


    def split(self):
        self.kill()

        if self.radius > ASTEROID_MIN_RADIUS:
            angle = random.uniform(20, 50)
            vel1 = self.velocity.rotate(angle)
            vel2 = self.velocity.rotate(-angle)
            asteroid1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            asteroid1.velocity = vel1 * 1.2
            asteroid2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            asteroid2.velocity = vel2 * 1.2
