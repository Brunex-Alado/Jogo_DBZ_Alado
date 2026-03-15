import pygame


# ~~ CORES DO JOGO ~~
C_ORANGE = (255, 128, 0)
C_YELLOW = (255, 255, 0)
C_WHITE = (255, 255, 255)
C_GREEN = (0, 200, 0)
C_CYAN = (0, 200, 200)


# ~~ TAMANHO DA JANELA ~~
WIN_WIDTH = 1200
WIN_HEIGHT = 300


# ~~ EVENTOS DO JOGO ~~
EVENT_ENEMY = pygame.USEREVENT + 1


# ~~ OPÇÕES DO MENU ~~
MENU_OPTION = (
    "Player",
    "Coop",
    "Score",
    "Exit"
)


# ~~ VELOCIDADE DAS ENTIDADES ~~
ENTITY_SPEED = {

    "Player1": 5,
    "Player2": 5,

    "Player1Shot": 10,
    "Player2Shot": 10,

    "Player1Ssj": 6,
    "Player2Ssj": 6,

    "Player1SsjShot": 14,
    "Player2SsjShot": 14,

    "Enemy": 3,
    "EnemyShot": 6,

    "Boss1": 2,
    "Boss1Shot": 9,

    "Boss2": 2,
    "Boss2Shot": 10,
}


# ~~ VIDA DAS ENTIDADES ~~
ENTITY_HEALTH = {

    "Player1": 100,
    "Player2": 100,

    "Player1Shot": 1,
    "Player2Shot": 1,

    "Player1Ssj": 150,
    "Player2Ssj": 150,

    "Player1SsjShot": 1,
    "Player2SsjShot": 1,

    "Enemy": 30,
    "EnemyShot": 1,

    "Boss1": 250,
    "Boss1Shot": 1,

    "Boss2": 250,
    "Boss2Shot": 1,
}


# ~~ DANO DAS ENTIDADES ~~
ENTITY_DAMAGE = {

    "Player1": 0,
    "Player2": 0,

    "Player1Shot": 15,
    "Player2Shot": 15,

    "Player1Ssj": 0,
    "Player2Ssj": 0,

    "Player1SsjShot": 15,
    "Player2SsjShot": 15,

    "Enemy": 10,
    "EnemyShot": 10,

    "Boss1": 25,
    "Boss1Shot": 20,

    "Boss2": 30,
    "Boss2Shot": 25,
}


# ~~ PONTUAÇÃO DAS ENTIDADES ~~
ENTITY_SCORE = {

    "Enemy": 300,
    "Boss1": 4000,
    "Boss2": 5000
}


# ~~ DELAY DE TIRO AUTOMÁTICO ~~
ENTITY_SHOT_DELAY = {

    "Player1": 20,
    "Player2": 20,

    "Player1Ssj": 12,
    "Player2Ssj": 12,

    "Enemy": 90,

    "Boss1": 60,
    "Boss2": 60,
}


# ~~ CONTROLES DOS PLAYERS ~~
PLAYER_KEY_UP = {
    "Player1": pygame.K_UP,
    "Player2": pygame.K_w,
    "Player1Ssj": pygame.K_UP,
    "Player2Ssj": pygame.K_w
}

PLAYER_KEY_DOWN = {
    "Player1": pygame.K_DOWN,
    "Player2": pygame.K_s,
    "Player1Ssj": pygame.K_DOWN,
    "Player2Ssj": pygame.K_s
}

PLAYER_KEY_LEFT = {
    "Player1": pygame.K_LEFT,
    "Player2": pygame.K_a,
    "Player1Ssj": pygame.K_LEFT,
    "Player2Ssj": pygame.K_a
}

PLAYER_KEY_RIGHT = {
    "Player1": pygame.K_RIGHT,
    "Player2": pygame.K_d,
    "Player1Ssj": pygame.K_RIGHT,
    "Player2Ssj": pygame.K_d
}