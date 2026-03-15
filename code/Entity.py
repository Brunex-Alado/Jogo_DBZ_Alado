from abc import ABC, abstractmethod
import pygame

from code.Const import ENTITY_HEALTH, ENTITY_DAMAGE, ENTITY_SCORE


class Entity(ABC):

    def __init__(self, name: str, position: tuple):

        self.name = name

        # ~~ CARREGA SPRITE AUTOMATICAMENTE ~~
        self.surf = pygame.image.load("./asset/" + name + ".png").convert_alpha()

        self.rect = self.surf.get_rect(
            left=position[0],
            top=position[1]
        )

        # ~~ ATRIBUTOS ~~
        self.health = ENTITY_HEALTH.get(self.name, 1)
        self.damage = ENTITY_DAMAGE.get(self.name, 0)
        self.score = ENTITY_SCORE.get(self.name, 0)

        self.last_dmg = None

    @abstractmethod
    def move(self):
        pass