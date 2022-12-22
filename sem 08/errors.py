class InvalidDataFormat(Exception):
    def __init__(self,message = "Invalid Data", *args: object) -> None:
        super().__init__(message, *args)

class InvalidCommand(Exception):
    def __init__(self,message = "Invalid Command", *args: object) -> None:
        super().__init__(message, *args)

class CharacterExists(Exception):
    def __init__(self,message = "Character already exists ", *args: object) -> None:
        super().__init__(message, *args)
        
class CharacterNotFound(Exception):
    def __init__(self,message = "Character not found", *args: object) -> None:
        super().__init__(message, *args)
        
class InvalidCharacterClass(Exception):
    def __init__(self,message = "Invalid Class", *args: object) -> None:
        super().__init__(message, *args)
        
class InvalidCharacterData(Exception):
    def __init__(self,message = "Invalid Class", *args: object) -> None:
        super().__init__(message, *args)

