from errors import CharacterExists

class Character:
    def __init__(self,name,gender,role,weapon, item):
        self.name = name
        self.gender = gender
        self.role = role
        self.weapon = weapon
        self.item = item
        self.characters = []
    def get_print(self):
        return f"Character({self.name},{self.gender},{self.role},{self.weapon},{self.item}, characters:[{len(self.characters)}])"
    def add_character(self,character ):
        if character in self.characters:
            raise CharacterExists("Error:This character already exist")
        self.characters.append(character)
