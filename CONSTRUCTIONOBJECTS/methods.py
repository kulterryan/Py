class Animal:
    def __init__(self,**kwargs):
        self._type = kwargs['type'] if 'type' in kwargs else 'Kitten'
        self._name = kwargs['type'] if 'type' in kwargs else 'Fluffy'
        self._sound = kwargs['type'] if 'type' in kwargs else 'Meow'
    
    def type(self, t = None):
        if t: self._type = t
        return self._type
    
    def name(self, n = None):
        if n: self._type = n
        return self._name
    
    def sound(self, s = None):
        if s: self._type = s
        return self._sound

    def __str__(self):
        return f'The {self.type()} in named "{self.name()}" and says "{self.name()}"'

def print_animal(a):
    if not isinstance(a, Animal):
        raise TypeError('print_Animal(): requires an Animal.')
    print(f'The {a.type()} is named "{a.name()}" and says "{a.sound()}"')

def main():
    print(Animal(type = 'Kitten', name = 'Fluffy', sound = 'Meow'))
    print(Animal(type = 'Goffy', name = "Doggie", sound = "Bhaw"))

if __name__ == "__main__":
    main()