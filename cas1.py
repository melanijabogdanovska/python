#the first excercise 
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
  def _init_ (self, **kwargs):
    if 'name' not in kwargs: raise MissingParameterError('name')
    if 'age' not in kwargs: raise MissingParameterError('age')
    if 'sound' not in kwargs: raise MissingParameterError('sound')
    if type(kwargs['name']) != str: raise InvalidParameterError('name')
    if type(kwargs['age']) != int: raise InvalidParameterError('age')
    if type(kwargs['sound']) != str: raise InvalidParameterError('sound')

    self.name = kwargs['name']
    self.age = kwargs['age']
    self.sound = kwargs['sound']

  def make_sound():
    print(f'{self.name} says {self.sound}!')

  def print():
    pass

  def daily_task():
    pass


class Jaguar(JungleAnimal):
  def __init__(self, **kwargs):
    super().__init__(kwargs)
    if kwargs['age'] > 15: raise InvalidAgeError()
