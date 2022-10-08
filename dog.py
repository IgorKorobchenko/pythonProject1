from animal import Animal

class Dog(Animal):
    def __init__(self, name, age, weight, breed = 'Terrier'):
        super().__init__(name, age, weight)#супер уже содержит в себе Self
        self.breed = breed

    def is_barking(self):
        print(f'{self.name} is barking')
