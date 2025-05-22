import pygame
from constants import *
from player import Player



class App:
    def __init__(self):
        self.__running = True
        self.__display_surf = None
        self.size = SCREEN_WIDTH, SCREEN_HEIGHT
        self.clock = None
        self.dt = None
        self.player = None

    def on_init(self):
        pygame.init()
        self.__display_surf = pygame.display.set_mode(self.size)
        self.__running = True
        self.clock = pygame.time.Clock()
        self.dt = 0
        self.player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.__running = False

    def on_loop(self):
        self.player.update(self.dt)
        pass

    def on_render(self):
        #Black out screen
        self.__display_surf.fill(BLACK)

        #Draw actors
        self.player.draw(self.__display_surf)


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
