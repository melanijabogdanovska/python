from random import randint, choice
class MissingParameterError(Exception):
  def __init__(self, parameter):
    self.message = f'Missing class parameter: {parameter}'
    super().__init__(self.message)


class InvalidParameterError(Exception):
  def __init__(self, parameter):
    self.message = f'Invalid class parameter: {parameter}'
    super().__init__(self.message)


class InvalidAgeError(InvalidParameterError):
  def __init__(self, parameter):
    super().__init__(parameter)

class InvalidSoundError(InvalidParameterError):
  def __init__(self, parameter):
    super().__init__(parameter)

class JungleAnimal():
  def __init__ (self, age, sound, name):

    self.age = age
    self.sound = sound
    self.name = name

    if 'age' not in self.age: raise MissingParameterError('age')
    if 'sound' not in self.sound: raise MissingParameterError('sound')
    if 'name' not in self.name: raise MissingParameterError('name')
    if type(self.age) != str: raise InvalidParameterError('age')
    if type(self.sound) != str: raise InvalidParameterError('sound')
    if type(self.name) != str: raise InvalidParameterError('name')


  def make_sound(self):
    print(f'{self.name} says {self.sound}!')

  def print(self):
    pass

  def daily_task(self):
    pass

class Jaguar(JungleAnimal):
    def __init__(self, age, sound, name):
        super().__init__(age, sound, name)
        if self.age > 15: raise InvalidAgeError()
        if not self.check_for_rs(self.sound): raise InvalidSoundError()

    def check_for_rs(self, string):
        r_count = 0
        for ch in string:
            if ch == 'r':
                r_count += 1
            if r_count == 2:
                return True
        return False

    def print(self):
        print(f"Jaguar({self.age}, {self.sound}, {self.name})")

    def daily_task(self,animals):
        for animal in range(len(animals)):
            if type(animals[animal]) == Human or type(animals[animal]) == Lemur:
                print(f" {self.name} the Jaguar hunted down {animals[animal].name} the {type(animals[animal]).__name__}")
                animals.remove(animal)
                break

class Lemur(JungleAnimal):
    def __init__(self, age, sound, name):
        super().__init__(age, sound, name)
        if self.age > 10: raise InvalidAgeError('age')
        if 'e' not in self.sound: raise InvalidSoundError()

    def print(self):
        print(f"Lemur({self.age}, {self.sound}, {self.name})")
  
    def daily_task(self, fruits):
        if fruits >= 10:
            print(f"{self.name} the Lemur ate a full meal of 10 fruits")
            return fruits - 10
    
        elif fruits > 0:
            print(f"{self.name} the Lemur could only find {fruits} fruits")
            return 0
    
        else:
            self.make_sound()
            print(f"{self.name} the Lemur couldn't find anything to eat")
            return 0

class Building:
    def __init__(self, type):
        self.type = type

class Human(JungleAnimal):
    def __init__(self, age, sound, name):
        super().__init__(age, sound, name)
        if self.age > 10: raise InvalidAgeError('age')
        if 'e' not in self.sound: raise InvalidSoundError('sound')

    def print(self):
        print(f"Human({self.age}, {self.sound}, {self.name})")

    def daily_task(self, animals, buildings):
        ind=animals.index(self)
        for ind in range(len(animals)):
            if ind == 0 and type(animals[ind + 1]) == Human:
                buildings.append(Building(f"type{ind}"))
            elif type(animals[ind - 1]) == Human and type (animals[ind + 1]) == Human:
                buildings.append(Building(f"type{ind}"))
            elif ind == len(animals - 1) and type(animals[ind - 1]) ==Human:
                buildings.append(Building(f"type{ind}"))
        return buildings

fruits = 100
animals = []
buildings = []

names = [
    "Jacob",
    "David",
    "Bobby",
    "Steve",
    "Johanssen",
    "Mac",
    "Jason",
    "Edward",
    "Alex",
    "Maddie",
    "Susan",
    "Abigail",
    "Jessica",
    "Lizzy",
    "Monica",
    "Lorelei",
    "Sandra",
    "Michelle"
]

sounds = [
    "RAAWR",
    "ROAR",
    "Grrr",
    "Shriek",
    "Meow",
    "Eeek",
    "Aaaaa",
    "Speak",
    "I am a Human"
]
for i in range(102):
    animal_rand = randint(0, 9)
    age_rand = randint(7, 20)
    try:
        if animal_rand in (0, 1, 2, 3):
            animals.append(Lemur(choice(names), age_rand, choice(sounds)))
        elif animal_rand in (4, 5, 6, 7):
            animals.append(Jaguar(choice(names), age_rand, choice(sounds)))
        else:
            animals.append(Human(choice(names), age_rand, choice(sounds)))
    except InvalidSoundError as e:
        print(e)
    except InvalidAgeError as e:
        print(e)
print(f"The jubgle now has {len(animals)} animals")

for anim in animals:
    if "Human" in repr(anim):
        anim.daily_task(anim, buildings)
    if "Lemur" in repr(anim):
        fruits = anim.daily_task(fruits)
    else:
        anim.daily_task(animals)

print(f'The Jungle now has {len(animals)} animals')
print(fruits)
print(animals)
print(buildings)
 
