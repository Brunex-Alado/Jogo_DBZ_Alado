import sys
import pygame
from pygame.font import Font
from code.Const import WIN_WIDTH


class Score:

    def __init__(self, window, score_value):

        self.window = window
        self.score_value = score_value
        self.background = pygame.image.load("./asset/ScoreBg.png").convert_alpha()


    def show(self):

        pygame.mixer.music.load("./asset/Score.mp3")
        pygame.mixer.music.set_volume(0.20)
        pygame.mixer.music.play(-1)

        while True:

            self.window.blit(self.background,(0,0))

            self.draw_outline_text("Parabens Alado Z",(WIN_WIDTH/2,120),40)
            self.draw_outline_text("Voce Salvou a Terra",(WIN_WIDTH/2,170),40)
            self.draw_outline_text("Seu Poder Final",(WIN_WIDTH/2,220),40)

            font = pygame.font.SysFont("Arial",50)

            score_surface = font.render(
                str(self.score_value),
                True,
                (255,255,255)
            )

            rect = score_surface.get_rect(center=(WIN_WIDTH/2,270))

            outline = font.render(str(self.score_value),True,(0,0,0))

            self.window.blit(outline,(rect.x-2,rect.y))
            self.window.blit(outline,(rect.x+2,rect.y))
            self.window.blit(outline,(rect.x,rect.y-2))
            self.window.blit(outline,(rect.x,rect.y+2))

            self.window.blit(score_surface,rect)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # ~~ BOTÃO ESC VOLTA PARA O MENU ~~
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return

            pygame.display.flip()


    def draw_outline_text(self,text,pos,size):

        font: Font = pygame.font.Font("./asset/Saiyan-Sans.ttf",size)

        base = font.render(text,True,(255,255,255))
        outline = font.render(text,True,(0,0,0))

        rect = base.get_rect(center=pos)

        self.window.blit(outline,(rect.x-2,rect.y))
        self.window.blit(outline,(rect.x+2,rect.y))
        self.window.blit(outline,(rect.x,rect.y-2))
        self.window.blit(outline,(rect.x,rect.y+2))

        self.window.blit(base,rect)