# class Employee:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#     def walk(self):
#         return "I can walk"
#
# class Developer(Employee):  # новый сласс Developer наследует от класса Employee
#     pass
#
# dev1 = Developer('Max', 'Popov')
# print(dev1.walk(), dev1.name)

# employee1 = Employee ('Alex', 'Popov') #задаем атрибуты этого класса. employee1 - экземпляр класса
# print(employee1.name, employee1.surname) #указыаем экзепляр класса и его атрибут
# print(employee1.walk())
#
# employee2 = Employee('MAx', 'Plank')

# class person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.name = surname
#
#     Person_1 = person('Alex', 'Popov')                         #создаем новый объект класса




# 5.1. Создайте любой класс с произвольным количеством подклассов, экземпляров, атрибутов и методов
#     - как минимум один атрибут должен быть с уровнем доступа private. Соответственно, для получания значений этого атрибута
#     нужно использовать методы get и set

# class vechicals: #создан класс
#     def __init__(self, brand_name, type): #атрибуты класса
#         self.brand_name = brand_name
#         self.type = type
#     def moving(self): # метод созданный внутри класса
#         return "Созданы для передвижения"
#
# class cabrio(vechicals): #объект внутри класса
#     def __init__(self, brand_name, type):
#         self.brand_name = brand_name
#         self.type = type
#     def pleassure (self):
#         return "Созданы для наслаждения"
#
# class budget_cabrio(cabrio):# наследует все от "деда" (vechicals) и "отца" (cabrio)
#     def __init__(self, brand_name, type, price):
#         super().__init__(brand_name, type)
#         self.price = price
#     def fun (self):
#         return "Удовольстие за доступные деньги"
#
# class trucks(vechicals):
#     def __init__(self, brand_name, type, model):
#         super().__init__(brand_name, type) # наследование от предка
#         self.model = model
#     def heavyduty (self):
#         return "Созданы для перевозки тяжелых грузов"
#
# print(issubclass(budget_cabrio,cabrio)) #проверка, что подкласс относится к высшему классу
# fancy_cars = cabrio('BMW', 'cabrio') #указан атрибут класса cabrio
# print(fancy_cars.brand_name, fancy_cars.type, fancy_cars.pleassure())
#
# cheap_cabrio = budget_cabrio('Fiat', 'cabrio', '$40k' )# объект ссылается на конструктор
# print(cheap_cabrio.brand_name, cheap_cabrio.type, cheap_cabrio.price, cheap_cabrio.fun())
# american_trucks = trucks('Ford', 'Truck', "F550")
# print(american_trucks.brand_name, american_trucks.model, american_trucks.heavyduty())
# # print(big_cars.brand_name, big_cars.type)

#Home work rewiev
from animal import Animal
from dog import Dog

animal = Animal(name='Tuzik', weight=100, age=2) #создание объекта класса
print(animal.__dict__)
print(animal.weight)
animal.print_info()
# print(Animal.Color) #вызов непосредственно из класса
# print(animal.Color) #вызов через объект класса
# animal.set_name('Lelik')

dog1 = Dog('Barbos', 5, 10, 'Yardterrier')
print(dog1.__dict__)
dog1.print_info()
dog1.is_barking()
