from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str):

        if entity_name == "Player1":
            return Player("Player1", (100, 140))

        if entity_name == "Player2":
            return Player("Player2", (100, 200))

        return None