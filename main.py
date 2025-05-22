import pygame
from constants import *

BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class App:
    def __init__(self):
        self.__running = True
        self.__display_surf = None
        self.size = SCREEN_WIDTH, SCREEN_HEIGHT

    def on_init(self):
        pygame.init()
        self.__display_surf = pygame.display.set_mode(self.size)
        self.__running = True
        self.clock = pygame.time.Clock()

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.__running = False

    def on_loop(self):
        pass

    def on_render(self):
        self.__display_surf.fill(WHITE)
        pygame.display.update()
        self.clock.tick(60)
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
