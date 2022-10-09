#списки
# l = []
#добавление в список с помощью .append
#l.append(23)
# l.append(34)
# b = [24, 67]
# l.extend(b)
# l.insert(1, 56)
# l.remove(34)
# l.pop(0)
# print (l.index(67))
# print (l.count(24))

# l.reverse
# l.sum
# print (l)
# lis = [1, 56, 2]
# lis.sort()
# print (lis)
#
# print(sorted(lis))
#list comprehention:
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# #создаем список обычным методом:
# newlist = []
#
# for x in fruits:
#     if "a" in x:
#         newlist.append(x)
# print(newlist)
#сокращенная форма или list comprehention:
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x for x in fruits if "a" in x]
# print(newlist)



# a = [a + b for a in 'list' if a != 's' for b in 'soup' if b != 'u']
# print (a)


# letters = ("apple", "banana", "cat")
# a, b, c = letters
# print (a, b, c)

# l = [1, 2, 3]
# # if 4 not in l:
# #     print('no 4')
# print('сколько в массиве элементов' + str(len(l)))

# l = "hI Mike"
# my_list = list(l)
# print (my_list)



#Home work
#3.1. Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3
# my_list = ['a', 'b', [1, 2, 3], 'd']
# print(*my_list[2])

# 3.2 Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
#    - получите сумму всех чисел,
#    - распечатайте все строки, где есть буква 'a'
#1 Задача - получите сумму всех чисел,


#через цикл for:
list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# sum = 0
# for i in list_1:
#     if type(i) == int or type(i) == float:
#         sum += i
# print ("the sum of all numbers in the list is", sum)
#через lamda:
list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]

result = list(filter(lambda x: isinstance(x, int), list_1))
print(sum(result))

# t_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# print('Original list: ', list_1)
# print('Sum of all numbers: ', sum([x for x in list_1 if type(x) == int ]))
# print('All words with a: ', [y for y in list_1 if type(y) == str and "a" in y])

#Примитивное решение:
# list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# print (list_1[2] + list_1[4] + list_1[6] + list_1[7])

#2 Задача  - распечатайте все строки, где есть буква 'a'
# list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]

# for string in list_1:
#     if type(string) == str:
#         if string.find('a') !=-1:
#             print(string)

#или

# list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# print ('all words with a:', [y for y in list_1 if type(y) == str and "a" in y])


# print(list(filter(lambda x: 'a' in x, list_1)))
# print(*filter(lambda x: isinstance(x, str), list_1)) #выводит все слова из списка
# print(sum(result))
# for item in list_1:
#     if 'a' in item:
#         print(item)


# b = sorted(list_1, key=lambda x: str(type(x)))
#list_1.sum([2], [4], [6], [7])

#print (list_1)
# # sum_of_numbers = sum(list_1[2:4])
# # print (sum_of_numbers)

#3.3. Превратите лист ['cat', 'dog', 'horse, 'cow'] в кортеж
# animals = ['cat', 'dog', 'horse', 'cow']
# animals = tuple(animals)
# print (animals)

# #наоборот
# animals = ('cat', 'dog', 'horse', 'cow')
# animals = list(animals)
# print(animals)

# 3.4. Напишите программу, которая определяет, какая семья больше.
#       1) Программа имеет два input() - например, family_1, family_2.
#       2) Членов семьи нужно перечислить через запятую.
#      Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')

# family_1 = input("Bедите членов семьи №1: \n").split(',')
# family_2 = input("Bедите членов семьи №2: \n").split(',')
# family_1_members = (len(family_1))
# family_2_members = (len(family_2))
# print(f"в первой семье {family_1_members} чл")
# print(f"во второй семье {family_2_members} чл")
# if family_1_members > family_2_members:
#     print("семья 1 больше семьи 2")
# elif family_2_members > family_1_members:
#     print ("семья 2 больше семьи 1")
# else:
#     print ('семьи равны')

# 3.5. Создайте словарь film c ключами title, director, year, budget, main_actor, slogan. В значения можете передать информацию
#     о вашем любимом фильме.
#     - распечатайте только ключи
#     - распечатайте только значения
#     - распечатайте пары ключ - значение

# film = {
#     'title': 'Once upon a time in Hollywood',
#     'director': 'Tarantino',
#     'year': '2019',
#     'budget':'$1000000',
#     'main_actor':'Brad Pitt',
#     'slogan': 'Push or die'
# }
# print(film)
# print(*film.keys())
# print(*film.values())
# print(*film.items())

#3.6. Найдите сумму всех значений в словаре my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}

# my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
# sum_dic = sum(my_dictionary.values())
# print(sum_dic)
#print (sum(my_dictionary.values())) #более элегантное

# sum_dic = (sum(my_dictionary[item] for item in my_dictionary))
# print (sum_dic)

#3.7. Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1]
# print(set([1, 2, 3, 4, 5, 3, 2, 1])) #решено!

# 3.8. Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
#      - найдите значения, которые встречаются в обоих множествах
#      - найдите значения, которые не встречаются в обоих множествах
     # - проверьте являются ли эти множества подмножествами друг друга
# set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
# set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
#
# print(set2.intersection(set1))
# print (set2.difference(set1))
# print(set2.issubset(set1))
# print(set1.issubset(set2))
# print(set2.issuperset(set1))
# print(set1.issuperset(set2))


# set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
# set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
# print(set1.intersection(set2))
# print(set1.difference(set2))
# print(set2.issuperset(set1))
# print(set1.issuperset(set2))
# print(set1.issubset(set2))




#Кортежи
#Создание кортежа
# mytuple = 1, 2, 3
# print (mytuple)
#
# my_tuple = (1, True, 'name', 25)
# print (my_tuple)
#
# name = 'Mark',
# print (name)

#показать индекс каждого элемента когда есть повторяющиеся
# mytuple = (1, True, 'name', None, 'name', 'name', 25)
# for (index,item) in enumerate (mytuple):
#     print (index, item)

#распечатка кортежа через цикл
# i = 0
# mytuple = (1, True, 'name', None, 'name', 'name', 25)
# while i < len(mytuple):
#     print(mytuple[i])
#     i += 1

# def sum_it(*args):
#     total = 0
#     for num in args:
#         total = total + num
#     return total
# print(sum_it(4, 5, 10, 6, 20))
#DICTIONARIES
# my_dict = {
#     'name': 'Anna',
#     'last_name': 'Pavlova',
#     'age': 30,
#     'department': 'IT'
# }
#смена значения ключа
# my_dict ['last_name'] = 'smirnova'
# print(my_dict)
# #длина словаря
# print(len(my_dict))
# #добавления ключа и значения
# my_dict['salary'] = 5000
# # print(my_dict)
# # print(my_dict.keys())
# # print(my_dict.values())
# # print(my_dict.items())
# print(my_dict.pop('salary'))
#запрос ключа + поясняющая фраза если ключ не будет найден
#print(my_dict.get('salary', 'Not found'))

# SETS
#print(set([1, 8, 2, 1, 5, 8, 9])) #выводим только уникальные значения
#
# print(set1.issubset(set2))
# print(set2.issuperset(set1))
# print(set2.intersection(set1))
# print(set2.difference(set1))
# print(set1)
# print(set1.remove(1))
# print(set1)
# print(set1.add(8))
# print(set1)

# new = [x*x for x in list_1 if x%2 == 0]
# print(new)
#
# # new_2 = filter(lambda x: isinstance(x, x%2 == 0), list_1)
# new_2 = []
# for x in list_1:
#     if x % 2 == 0:
#         new_2.append(x * x)
# print(new_2)

# tuple_0 = ('Mark',)
# print(type(tuple_0))
# tuple_1 = ('Mark', 26, ['314 N 11Ln', 'LA', 85954])
# print(tuple_1)
# list_3 = list(tuple_1)
# print(list_3)
# list_3[1] = 27
# print(list_3)
# tuple_1 = tuple(list_3)
# print(tuple_1)
# tuple_1[2][-1] = 85955
# print(tuple_1)

# list_1 = [1, 2, 3, 4, 5, 6, 7] #переводим список в словарь, присваивая индекс каждому значению
# dict_1 = {}
# for ind in range(len(list_1)):
#     dict_1[ind] = list_1[ind]
# print(dict_1)
# #
# print(dict_1.keys()) #берем из словаря только ключи
# print(dict_1.values()) #берем из словаря только значения
# print(dict_1.items()) #когда берем и ключи и значения
#
# for ind, val in enumerate(dict_1.items(), 100):
#     print(f'{ind} ---> {val}')
#
# print(dict_1.get(1))