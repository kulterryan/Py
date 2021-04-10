class Animal:
    def __init__(self,type, name, sound):
        self._type = type
        self._name = name
        self._sound = sound
    
    def type(self):
        return self._type
    
    def name(self):
        return self._name
    
    def sound(self):
        return self._sound

def print_animal(a):
    if not isinstance(a, Animal):
        raise TypeError('print_Animal(): requires an Animal.')
    print(f'The {a.type()} is named "{a.name()}" and says "{a.sound()}"')

def main():
    print_animal(Animal('Kitten', 'Fluffy', 'Meow'))
    print_animal(Animal('Goffy', "Doggie", "Bhaw"))

if __name__ == "__main__":
    main()