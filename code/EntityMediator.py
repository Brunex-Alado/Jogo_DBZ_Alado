from code.Player import Player
from code.PlayerShot import PlayerShot
from code.Enemy import Enemy
from code.EnemyShot import EnemyShot
from code.Boss import Boss
from code.Boss2 import Boss2


# ~~ CLASSE RESPONSÁVEL PELAS INTERAÇÕES ENTRE ENTIDADES ~~
class EntityMediator:


    # ~~ DETECÇÃO DE COLISÕES ENTRE ENTIDADES ~~
    @staticmethod
    def verify_collision(entity_list):

        for i in range(len(entity_list)):

            ent1 = entity_list[i]

            for j in range(i + 1, len(entity_list)):

                ent2 = entity_list[j]

                if ent1.rect.colliderect(ent2.rect):

                    # ~~ PLAYER SHOT ACERTA ENEMY ~~
                    if isinstance(ent1, PlayerShot) and isinstance(ent2, Enemy):

                        ent1.health = 0
                        ent2.health -= ent1.damage
                        ent2.last_dmg = ent1.name

                    elif isinstance(ent2, PlayerShot) and isinstance(ent1, Enemy):

                        ent2.health = 0
                        ent1.health -= ent2.damage
                        ent1.last_dmg = ent2.name


                    # ~~ PLAYER SHOT ACERTA BOSS1 ~~
                    if isinstance(ent1, PlayerShot) and isinstance(ent2, Boss):

                        ent1.health = 0
                        ent2.health -= ent1.damage
                        ent2.last_dmg = ent1.name

                    elif isinstance(ent2, PlayerShot) and isinstance(ent1, Boss):

                        ent2.health = 0
                        ent1.health -= ent2.damage
                        ent1.last_dmg = ent2.name


                    # ~~ PLAYER SHOT ACERTA BOSS2 ~~
                    if isinstance(ent1, PlayerShot) and isinstance(ent2, Boss2):

                        ent1.health = 0
                        ent2.health -= ent1.damage
                        ent2.last_dmg = ent1.name

                    elif isinstance(ent2, PlayerShot) and isinstance(ent1, Boss2):

                        ent2.health = 0
                        ent1.health -= ent2.damage
                        ent1.last_dmg = ent2.name


                    # ~~ TIRO DO INIMIGO ACERTA PLAYER ~~
                    if isinstance(ent1, EnemyShot) and isinstance(ent2, Player):

                        ent1.health = 0
                        ent2.health -= ent1.damage

                    elif isinstance(ent2, EnemyShot) and isinstance(ent1, Player):

                        ent2.health = 0
                        ent1.health -= ent2.damage


    # ~~ DAR SCORE AO PLAYER QUE MATOU O INIMIGO ~~
    @staticmethod
    def give_score(enemy, entity_list):

        if enemy.last_dmg == "Player1Shot" or enemy.last_dmg == "Player1SsjShot":

            for ent in entity_list:
                if ent.name.startswith("Player1"):
                    ent.score += enemy.score

        elif enemy.last_dmg == "Player2Shot" or enemy.last_dmg == "Player2SsjShot":

            for ent in entity_list:
                if ent.name.startswith("Player2"):
                    ent.score += enemy.score


    # ~~ REMOVER ENTIDADES MORTAS ~~
    @staticmethod
    def verify_health(entity_list):

        for ent in entity_list[:]:

            if ent.health <= 0:

                if isinstance(ent, (Enemy, Boss, Boss2)):

                    EntityMediator.give_score(ent, entity_list)

                entity_list.remove(ent)