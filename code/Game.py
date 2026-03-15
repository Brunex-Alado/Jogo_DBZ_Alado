import sys
import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Menu import Menu
from code.Level import Level
from code.Score import Score


class Game:

    def __init__(self):

        pygame.init()

        pygame.display.set_caption("DB Alado")

        self.window = pygame.display.set_mode(
            (WIN_WIDTH, WIN_HEIGHT)
        )


    def run(self):

        while True:

            menu = Menu(self.window)

            menu_return = menu.run()


            if menu_return == MENU_OPTION[0]:

                level = Level(self.window,"Level1","Player")

                result = level.run()

                if result:

                    level = Level(self.window,"Level2","Player")

                    score_value = level.run()

                    Score(self.window,score_value).show()


            elif menu_return == MENU_OPTION[1]:

                level = Level(self.window,"Level1","Coop")

                result = level.run()

                if result:

                    level = Level(self.window,"Level2","Coop")

                    score_value = level.run()

                    Score(self.window,score_value).show()


            elif menu_return == MENU_OPTION[2]:

                Score(self.window,0).show()


            elif menu_return == MENU_OPTION[3]:

                pygame.quit()
                sys.exit()