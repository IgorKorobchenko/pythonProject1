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
#         return "Удовольствие за доступные деньги"
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
# print(trucks.__dict__)
#
# #Home work rewiev (OOP principles)


