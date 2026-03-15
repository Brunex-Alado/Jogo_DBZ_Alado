import random

from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY, WIN_WIDTH, WIN_HEIGHT
from code.Entity import Entity
from code.EnemyShot import EnemyShot


class Enemy(Entity):

    def __init__(self, name: str, position: tuple):

        super().__init__(name, position)

        self.shot_delay = ENTITY_SHOT_DELAY.get(self.name, 120)

    def move(self):

        self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self):

        self.shot_delay -= 1

        if self.shot_delay <= 0:

            self.shot_delay = ENTITY_SHOT_DELAY.get(self.name, 120)

            return EnemyShot(
                name="EnemyShot",
                position=(self.rect.centerx, self.rect.centery)
            )

        return None