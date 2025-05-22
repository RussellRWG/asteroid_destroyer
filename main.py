import pygame
from constants import *
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField
from shot import Shot



class App:
    def __init__(self):
        self.__running = True
        self.__display_surf = None
        self.size = SCREEN_WIDTH, SCREEN_HEIGHT
        self.clock = None
        self.dt = None
        self.player = None
        self.asteroidfield = None
        self.updatable = pygame.sprite.Group()
        self.drawable = pygame.sprite.Group()
        self.asteroids = pygame.sprite.Group()
        self.shots = pygame.sprite.Group()

    def on_init(self):
        pygame.init()
        self.__display_surf = pygame.display.set_mode(self.size)
        self.__running = True
        self.clock = pygame.time.Clock()
        self.dt = 0
        AsteroidField.containers = (self.updatable)
        Asteroid.containers = (self.asteroids, self.updatable, self.drawable)
        Player.containers = (self.updatable, self.drawable)
        Shot.containers = (self.updatable, self.drawable, self.shots)
        self.player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        self.asteroidfield = AsteroidField()

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.__running = False

    def on_loop(self):
        self.updatable.update(self.dt)


        for asteroid in self.asteroids:
            if asteroid.check_collision(self.player):
                print("Game over!")
                self.__running = False

            for shot in self.shots:
                if asteroid.check_collision(shot):
                    asteroid.split()
                    shot.kill()

    def on_render(self):
        #Black out screen
        self.__display_surf.fill(BLACK)

        #Draw actors
        for actor in self.drawable:
            actor.draw(self.__display_surf)


        #Update screen and tick the clock
        pygame.display.update()
        self.dt = self.clock.tick(60)/1000
        pass

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self.__running = False

        while(self.__running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()



if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
