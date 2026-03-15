import sys
import pygame
import random

from pygame import Surface
from pygame.font import Font

from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Player import Player
from code.Entity import Entity
from code.Enemy import Enemy
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Boss import Boss
from code.Boss2 import Boss2


class Level:

    def __init__(self, window: Surface, level_name: str, game_mode: str):

        self.window = window
        self.level_name = level_name

        self.background = pygame.image.load(
            f"./asset/{level_name}Bg.png"
        ).convert()

        self.entity_list: list[Entity] = []

        self.enemy_kills = 0
        self.boss_spawned = False

        player = EntityFactory.get_entity("Player1")
        self.entity_list.append(player)

        if game_mode == "Coop":
            player = EntityFactory.get_entity("Player2")
            self.entity_list.append(player)

        pygame.time.set_timer(pygame.USEREVENT + 1, 2000)


    def run(self):

        pygame.mixer.music.load(f"./asset/{self.level_name}.mp3")
        pygame.mixer.music.set_volume(0.20)
        pygame.mixer.music.play(-1)

        clock = pygame.time.Clock()

        while True:

            clock.tick(60)

            self.window.blit(self.background,(0,0))

            boss_entity = None

            for ent in self.entity_list:

                self.window.blit(ent.surf,ent.rect)

                ent.move()

                if isinstance(ent,(Boss,Boss2)):
                    boss_entity = ent

                if isinstance(ent,Player):

                    shot = ent.shoot()

                    if shot:
                        self.entity_list.append(shot)

                    self.draw_player_hud(ent)

                if isinstance(ent,(Enemy,Boss,Boss2)):

                    shot = ent.shoot()

                    if shot:
                        self.entity_list.append(shot)

            if boss_entity:
                self.draw_boss_hud(boss_entity)


            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.USEREVENT + 1 and not self.boss_spawned:

                    enemy = Enemy(
                        "Enemy",
                        (WIN_WIDTH+50,random.randint(50,WIN_HEIGHT-50))
                    )

                    self.entity_list.append(enemy)


            # ~~ COLISÕES ~~
            EntityMediator.verify_collision(self.entity_list)

            # ~~ CONTAR ENEMY MORTOS ANTES DE REMOVER ~~
            for ent in self.entity_list:
                if isinstance(ent, Enemy) and ent.health <= 0:
                    self.enemy_kills += 1


            # ~~ REMOVER ENTIDADES MORTAS ~~
            EntityMediator.verify_health(self.entity_list)


            # ~~ SPAWN DO BOSS APÓS 10 ENEMY ~~
            if self.enemy_kills >= 10 and not self.boss_spawned:

                self.spawn_boss()


            # ~~ VERIFICAR MORTE DO BOSS ~~
            if self.boss_spawned:

                if self.level_name == "Level1":

                    if not any(isinstance(ent,Boss) for ent in self.entity_list):
                        return True

                else:

                    if not any(isinstance(ent,Boss2) for ent in self.entity_list):

                        final_score = 0

                        for ent in self.entity_list:
                            if isinstance(ent,Player):
                                final_score = ent.score

                        return final_score

            pygame.display.flip()


    def spawn_boss(self):

        if self.level_name == "Level1":

            boss = Boss("Boss1",(WIN_WIDTH+150,WIN_HEIGHT/2))
            pygame.mixer.music.load("./asset/Level1Boss.mp3")

        else:

            boss = Boss2("Boss2",(WIN_WIDTH+150,WIN_HEIGHT/2))
            pygame.mixer.music.load("./asset/Level2Boss.mp3")

        pygame.mixer.music.set_volume(0.20)
        pygame.mixer.music.play(-1)

        self.entity_list.append(boss)
        self.boss_spawned = True

        for ent in self.entity_list:

            if ent.name == "Player1":

                ent.name = "Player1Ssj"
                ent.surf = pygame.image.load("./asset/Player1Ssj.png").convert_alpha()
                ent.health = 150

            if ent.name == "Player2":

                ent.name = "Player2Ssj"
                ent.surf = pygame.image.load("./asset/Player2Ssj.png").convert_alpha()
                ent.health = 150


    def draw_player_hud(self,player):

        font_text = pygame.font.Font("./asset/Saiyan-Sans.ttf",18)
        font_num = pygame.font.SysFont("Arial",18)

        x = 20
        y = 10

        if "Ssj" in player.name:
            label = "Nivel de Poder Eh Mais de"
            value = "8000"
        else:
            label = "Nivel de Poder"
            value = "3000"

        self.draw_outline_text(label,(x,y),font_text)
        self.draw_outline_number(value,(x+260,y),font_num)

        max_hp = 150 if "Ssj" in player.name else 100
        hp_ratio = player.health/max_hp

        pygame.draw.rect(self.window,(0,0,0),(x,y+30,120,10))
        pygame.draw.rect(self.window,(0,255,0),(x,y+30,120*hp_ratio,10))


    def draw_boss_hud(self,boss):

        font_text = pygame.font.Font("./asset/Saiyan-Sans.ttf",18)
        font_num = pygame.font.SysFont("Arial",18)

        x = WIN_WIDTH-300
        y = 10

        label = "Nivel de Poder"

        self.draw_outline_text(label,(x,y),font_text)
        self.draw_outline_number("6000",(x+180,y),font_num)

        hp_ratio = boss.health/250

        pygame.draw.rect(self.window,(0,0,0),(x,y+30,120,10))
        pygame.draw.rect(self.window,(255,0,0),(x,y+30,120*hp_ratio,10))


    def draw_outline_text(self,text,pos,font):

        base = font.render(text,True,(255,255,255))
        outline = font.render(text,True,(0,0,0))

        rect = base.get_rect(topleft=pos)

        self.window.blit(outline,(rect.x-2,rect.y))
        self.window.blit(outline,(rect.x+2,rect.y))
        self.window.blit(outline,(rect.x,rect.y-2))
        self.window.blit(outline,(rect.x,rect.y+2))

        self.window.blit(base,rect)


    def draw_outline_number(self,text,pos,font):

        base = font.render(text,True,(255,255,255))
        outline = font.render(text,True,(0,0,0))

        rect = base.get_rect(topleft=pos)

        self.window.blit(outline,(rect.x-2,rect.y))
        self.window.blit(outline,(rect.x+2,rect.y))
        self.window.blit(outline,(rect.x,rect.y-2))
        self.window.blit(outline,(rect.x,rect.y+2))

        self.window.blit(base,rect)