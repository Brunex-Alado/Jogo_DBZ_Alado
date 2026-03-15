from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY
from code.Entity import Entity
from code.EnemyShot import EnemyShot


# ~~ CLASSE DO SEGUNDO CHEFE DO JOGO ~~
class Boss2(Entity):

    def __init__(self, name: str, position: tuple):

        super().__init__(name, position)

        # ~~ DELAY DE TIRO DO BOSS2 ~~
        self.shot_delay = ENTITY_SHOT_DELAY[self.name] + 120

        # ~~ DIREÇÃO DO MOVIMENTO VERTICAL ~~
        self.direction = 1


    # ~~ MOVIMENTO DO BOSS2 ~~
    def move(self):

        # ~~ ENTRADA DO BOSS NA TELA ~~
        if self.rect.centerx > 900:
            self.rect.centerx -= ENTITY_SPEED[self.name]

        else:

            # ~~ MOVIMENTO VERTICAL ~~
            self.rect.centery += self.direction * 3

            if self.rect.top <= 20:
                self.direction = 1

            if self.rect.bottom >= 280:
                self.direction = -1


    # ~~ SISTEMA DE TIRO DO BOSS2 ~~
    def shoot(self):

        self.shot_delay -= 1

        if self.shot_delay <= 0:

            self.shot_delay = ENTITY_SHOT_DELAY[self.name] + 120

            return EnemyShot(
                name="Boss2Shot",
                position=(self.rect.centerx, self.rect.centery)
            )

        return None