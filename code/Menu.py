# ~~ IMPORTS ~~
import sys
import pygame

from pygame import Surface
from pygame.font import Font

from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Const import MENU_OPTION
from code.Const import C_WHITE, C_YELLOW

from code.AssetLoader import resource_path


class Menu:

    def __init__(self, window: Surface):

        self.window = window

        # ~~ CARREGA BACKGROUND ~~
        self.surf = pygame.image.load(
            resource_path("asset/MenuBg.png")
        ).convert()

        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):

        # ~~ MÚSICA DO MENU ~~
        pygame.mixer.music.load(
            resource_path("asset/Menu.mp3")
        )

        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)

        menu_option = 0

        clock = pygame.time.Clock()

        while True:

            clock.tick(60)

            self.window.blit(self.surf, self.rect)


            # ~~ TÍTULO ~~
            self.draw_text_outline(
                70,
                "DB Alado",
                C_YELLOW,
                (WIN_WIDTH / 2, 70)
            )


            # ~~ MENU CENTRAL ~~
            menu_start_y = 140
            menu_spacing = 35

            options = [
                "Player",
                "Coop",
                "Score",
                "Exit"
            ]

            for i in range(len(options)):

                color = C_WHITE

                if i == menu_option:
                    color = C_YELLOW

                self.draw_text_outline(
                    36,
                    options[i],
                    color,
                    (WIN_WIDTH / 2, menu_start_y + i * menu_spacing)
                )


            # ~~ CONTROLES ~~
            self.draw_text_outline(
                18,
                "SETAS ou WASD para navegar",
                C_WHITE,
                (WIN_WIDTH - 180, WIN_HEIGHT - 60)
            )

            self.draw_text_outline(
                18,
                "SPACE confirmar",
                C_WHITE,
                (WIN_WIDTH - 180, WIN_HEIGHT - 40)
            )

            self.draw_text_outline(
                18,
                "ESC voltar",
                C_WHITE,
                (WIN_WIDTH - 180, WIN_HEIGHT - 20)
            )


            # ~~ CRÉDITOS ACADÊMICOS ~~
            self.draw_text_outline_arial(
                18,
                "RU 4961408",
                (255,255,255),
                (100, WIN_HEIGHT - 40)
            )

            self.draw_text_outline_arial(
                18,
                "Bruno de Sousa Silva",
                (255,255,255),
                (140, WIN_HEIGHT - 20)
            )


            # ~~ TÍTULO ACADÊMICO ~~
            self.draw_text_outline(
                20,
                "Uninter - ADS",
                C_WHITE,
                (120, 20)
            )

            self.draw_text_outline(
                18,
                "Projeto Academico",
                C_WHITE,
                (140, 40)
            )

            pygame.display.flip()


            # ~~ EVENTOS ~~
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:

                    if event.key in (pygame.K_DOWN, pygame.K_s):

                        if menu_option < len(options) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0

                    if event.key in (pygame.K_UP, pygame.K_w):

                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(options) - 1

                    if event.key == pygame.K_SPACE:
                        return MENU_OPTION[menu_option]

                    if event.key == pygame.K_ESCAPE:
                        return MENU_OPTION[3]


    # ~~ TEXTO COM CONTORNO (SAIYAN FONT) ~~
    def draw_text_outline(self, size, text, color, center):

        font: Font = pygame.font.Font(
            resource_path("asset/Saiyan-Sans.ttf"),
            size
        )

        text_surface = font.render(text, True, color)
        outline_surface = font.render(text, True, (0,0,0))

        rect = text_surface.get_rect(center=center)

        for dx in [-2,-1,1,2]:
            for dy in [-2,-1,1,2]:
                outline_rect = rect.copy()
                outline_rect.x += dx
                outline_rect.y += dy
                self.window.blit(outline_surface, outline_rect)

        self.window.blit(text_surface, rect)


    # ~~ TEXTO ARIAL COM CONTORNO ~~
    def draw_text_outline_arial(self, size, text, color, center):

        font = pygame.font.SysFont("Arial", size)

        text_surface = font.render(text, True, color)
        outline_surface = font.render(text, True, (0,0,0))

        rect = text_surface.get_rect(center=center)

        for dx in [-1,1]:
            for dy in [-1,1]:
                outline_rect = rect.copy()
                outline_rect.x += dx
                outline_rect.y += dy
                self.window.blit(outline_surface, outline_rect)

        self.window.blit(text_surface, rect)