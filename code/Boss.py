from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY
from code.Entity import Entity
from code.EnemyShot import EnemyShot


# ~~ CLASSE DO CHEFE DO LEVEL ~~
class Boss(Entity):

    def __init__(self, name: str, position: tuple):

        super().__init__(name, position)

        # ~~ DELAY DE TIRO DO BOSS (2 SEGUNDOS MAIS LENTO) ~~
        # 60 FPS x 2 = 120 FRAMES
        self.shot_delay = ENTITY_SHOT_DELAY[self.name] + 120

        # ~~ DIREÇÃO DO MOVIMENTO VERTICAL ~~
        self.direction = 1

    # ~~ MOVIMENTO DO BOSS ~~
    def move(self):

        # ~~ ENTRADA DO BOSS NA TELA (MOVIMENTO HORIZONTAL) ~~
        if self.rect.centerx > 900:
            self.rect.centerx -= ENTITY_SPEED[self.name]

        # ~~ MOVIMENTO VERTICAL CONTÍNUO ~~
        else:

            self.rect.centery += self.direction * 2

            # ~~ LIMITE SUPERIOR ~~
            if self.rect.top <= 20:
                self.direction = 1

            # ~~ LIMITE INFERIOR ~~
            if self.rect.bottom >= 280:
                self.direction = -1

    # ~~ SISTEMA DE TIRO DO BOSS ~~
    def shoot(self):

        self.shot_delay -= 1

        if self.shot_delay <= 0:

            # ~~ RESET DO DELAY DE TIRO ~~
            self.shot_delay = ENTITY_SHOT_DELAY[self.name] + 180

            return EnemyShot(
                name="Boss1Shot",
                position=(self.rect.centerx, self.rect.centery)
            )

        return None