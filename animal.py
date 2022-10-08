class Animal:
    Color = 'Grey'
    def __init__(self, name='Animal', age=0, weight=0): #это атрибуты или свойства класса
        self.name = name #закрываем имя (__)_
        self.age = age
        self.weight = weight
        print('Create object of Animal class')

    def print_info(self): #создание метода
        print(f'Name of the animal is {self.name} with weight {self.weight} kg and age {self.age} years old')

    # def get_name(self):
    #     return self.__name if self.__name else None #построение логики через скрытие имени и метод get
    #
    # def set_name(self, name):
    #     self.__name = name
    #     self.Color = 'blue'

