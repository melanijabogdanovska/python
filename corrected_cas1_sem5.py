from random import randint, choice

class InvalidParameterError:
    def __init__(self, name):
        self.name = name
        raise Exception(f"Invalid class parameter: {self.name}")

class InvalidAgeError(InvalidParameterError):
    def __init__(self, age):
        super().__init__(age)

class InvalidSoundError(InvalidParameterError):
    def __init__(self, sound):
        super().__init__(sound)


class Building:
    def __init__(self, type):
        self.type = type



class JungleAnimal:
    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.sound = sound.lower()

        if type(self.name) != str:
            InvalidParameterError(self.name)
        if type(self.age) != int:
            InvalidAgeError(self.age)
        if type(self.sound) != str:
            InvalidSoundError(self.sound)

    def make_sound(self):
        print(f"{self.name} says {self.sound}!")

    def print(self):
        pass

    def daily_task(self):
        pass

class Jaguar(JungleAnimal):
    def __init__(self, name, age, sound):
        super().__init__(name, age, sound)
        if self.age > 15:
            InvalidAgeError(self.age)
        if self.sound.count("r") < 2:
            InvalidSoundError(self.sound)

    def __repr__(self):
        return f"Jaguar {self.name} {self.age} {self.sound}"

    def print(self):
        print(f"Jaguar({self.name} {self.age} {self.sound})")

    def daily_task(self, animals):
        for animal in animals:
            if repr(animal) != self.__repr__():
                animals.remove(animal)
                print(f"{self.name} the Jaguar haunted down {animal.name} the {animal.__class__.__name__}")

class Lemur(JungleAnimal):
    def __init__(self, name, age, sound):
        super().__init__(name, age, sound)
        if self.age > 10:
            InvalidAgeError(self.age)
        if not ("e" in self.sound):
            InvalidSoundError(self.sound)

    def __repr__(self):
        return f"Lemur {self.name} {self.age} {self.sound}"

    def print(self):
        print(f"Lemur({self.name}, {self.age}, {self.sound}")

    def daily_task(self, fruits):
        if fruits >= 10:
            print(f"{self.name} the Lemur ate a ful meal of 10 fruits")
            return fruits - 10

        elif 0 < fruits < 10:
            print(f"{self.name} the Lemur could only find {fruits} fruits")
            return 0

        else:
            for i in range(2):
                self.make_sound()
            print(f"{self.name} the Lemur couldnt find anythig to eat")
            return 0

class Human(JungleAnimal):
    def __init__(self, name, age, sound):
        super().__init__(name, age, sound)
        if self.age > 10:
            InvalidAgeError(self.age)
        if not ("e" in self.sound):
            InvalidSoundError(self.sound)
        
        def __repr__(self):
            return f"Human {self.name} {self.age} {self.sound}"

        def print(self):
            print(f"Human({self.name}, {self.age}, {self.sound})")

        def daily_task(self, animals, buildings):
            n = len(animals)
            for i in range(n):
                if repr(animals[i]) == "Human":
                    if i == 0 and repr(animals[i + 1]) == "Human":
                        buildings.append(Building(f"type{i}"))
                    elif i == n - 1 and repr(animals[i - 1]) == "Human":
                        buildings.append(Building(f"type{i}"))
                    elif 0 < i < n - 1 and repr(animals[i - 1]) == "Human" and repr(animals[i + 1]) == "Human":
                        buildings.append(Building(f"type{i}"))
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
    if animal_rand in (0, 1, 2, 3):
        animals.append(Lemur(choice(names), age_rand, choice(sounds)))
    elif animal_rand in (4, 5, 6, 7):
        animals.append(Jaguar(choice(names), age_rand, choice(sounds)))
    else:
        animals.append(Human(choice(names), age_rand, choice(sounds)))
        
print(f"The jubgle now has {len(animals)} animals")

for animal in animals:
    if "Human" in repr(animal):
        animal.daily_task(animal, buildings)
    if "Lemur" in repr(animal):
        fruits = animal.daily_task(fruits)
    else:
        animal.daily_task(animals)

print(len(animals))
print(fruits)
print(animals)
print(buildings)