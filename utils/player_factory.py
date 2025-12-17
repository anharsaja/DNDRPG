from core.player import Player
from data.characters import characters

def create_player(character_name):
    for char in characters:
        if char["name"] == character_name:
            return Player(
                name=char["name"],
                hp=char["hp"],
                atk=char["atk"],
                defense=char["def"]
            )
    return None
