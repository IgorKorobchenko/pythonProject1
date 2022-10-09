# Функции и модули
#когда важен порядок аргументов:
# def person(age, last_name, name):
#     return f'Hello, my name is {name} {last_name}. I am {age} years old.'
# print (person(130, "LInkoln", "Abraham"))
# #когда не важен порядок аргументов:
# def person(age, last_name = 'linkoln', name = 'Abraham'):
#     return f'Hello, my name is {name} {last_name}. I am {age} years old.'
# print (person(130)) #позиционный аргумент должен идти до именованного
#
# print (person(name='Abraham', age=30)) #порядок не важен когда идет прямое обращение к аргументу

# def pattern(length, char1='-', char2='*'):
#     return(char1 + char2)*length + char1
# print(pattern(char2='/', length=9))

# ПРОСТРАНСТВО ИМЕН (SCOPE)
# x = 15
# y = 78
# def sum_it(x, y):
#     print(f'Locals: {locals()}') #выводит значения локальных переменных
#     return x + y
#
# print(f'Inside the function: {sum_it(5, 8)}')
# print(f'Outside the function: {x + y}')
# print(f'Globals: {globals()}') #выводит глобальные

#Анонимные фунции LAMDA выражение:
#print ((lambda x, y: x*y)(5, 8))
#or
# mult = lambda x, y: x*y
# print(mult(5, 8))

# print('------Sum list_1 With function and for loop----------')
# list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100] #решение через цикл
# def filter_and_sum_nums(l):
#     new_l = []
#     for i in l:
#         if isinstance(i, int):
#             new_l.append(i)
#     return sum(new_l)
#
# print(filter_and_sum_nums(list_1))
# list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# # print('--------Sum list_1 with lambda and filter----------')
# print(sum((filter(lambda x: isinstance(x, int), list_1)))) #решение через Lambda

# list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
#
# def take_odd(num):
#    if  isinstance(num, int) and num%2:
#         return True
#    return False
# print(list(filter(take_odd, list_1))) #скармливаем функцию take_odd функции высшего порядка filter

# list_3 = [1, 2, 5, 8, 10, 105, 78]
# list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# print('-----Filer odd_nums with lambda----------')
#
# filtered = list(filter(lambda x: isinstance(x, int), list_1))
#
# print(list(filter(lambda x: x%2, filtered)))
#
# print(list(filter(lambda x: x%2, list_3)))

# print('-----Filer strings with "a" using custom function ----------')
# list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# new_l = []
# for item in list_1:
#     if isinstance(item, str) and 'a' in item:
#         new_l.append(item)
# print(new_l)

# print('-----Filer strings with "a" using lambda ----------')
# list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# filtered = list(filter(lambda x: isinstance(x, str), list_1))
# print(list(filter(lambda x: 'a' in x, filtered)))

 # MODULES
# import functools
# from functools import reduce
# res = reduce(lambda x, y: x*y, [1, 5, 8, 11, 13]) #reduce применяет сложение или умножение или другие операции для всего выражения
# print(res)

# from myfile import * #(* значит импортировать все из файла)
# res = sum_it(5,8)
# print(res)
#
# res1 = prod(5, 8)
# print(res1)

# from math import *
# import math as m #другой вариант импорта через придуманное значение
# arr = [1, 2, 3, 4, 5, 10, 25]
# new_arr = m.prod(arr)
# print(new_arr)

# from myfile import *
# def tests():
#     assert sum_it(5, 8) == 13, f'Wrong number, actual result is {sum_it(5,8)}'
#     assert prod(10, 6) == 60, f'Wrong number, actual result is {prod(10,6)}'
#     assert div(10, 0) == "Can't devide by zero" #Home wor

# import datetime
# birth_year = 1980
# current_year = datetime.date.today()
# # current_age = current_date.year - birth_year
# current_month = datetime.date.month
# print(current_date)
# print((current_age))
# print(current_month)

# def sum_it(**kwargs):
    # result = 0
    # for i in kwargs.values():
    #     result += i
#     return result
# print(sum_it(num1=4, num2=5, num3=10))

# def sum_it(**kwargs): # ** - распаковка словаря с передачей именоанных аргументов в формате ключ+значение, kwargs - имя
#     return sum(kwargs.values())
# print(sum_it(num1=4, num2=5, num3=10))

# def sum_i(*args):
#     print(type(args))
#     return sum(args)
# print(sum_i(5, 6, 10))
# list_2 = [1, 2, 3, 4, 5]
# print(list(map(lambda x: x*x, list_2)))#map-фильтр (функция высшего порядка) применяет действие ко всем элементам листа
# print([x*x for x in list_2]) #тоже действие но без map

# Домашка

# #4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
#      периметр квадрата, площадь квадрата и диагональ квадрата.
# *args нужен, когда мы хотим передать неизвестное количество неименованных аргументов.
# Если поставить * перед именем, это имя будет принимать не один аргумент, а несколько.

# import math
#
# def square(side, *args):
#     print((side * side), (side * 4), (2*(math.sqrt(2))))
#
# square(5) #вызов функции и ввод аргументов

#чужое решение:
# import math as m
# def square(side):
#     return (side * 4, side ** 2, round (m.sqrt(side **2)), 2)
# square_data = square(int(input("inpute square side:")))
# print(f'square area:){square_data[0]}, perimetr: {square_data[1]}, diagonal {square_data[2]}')
# print(square(9))



# 4.2. Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно
#      в формате аргумент: значение. Например:
# 	name: John
# 	last_name: Smith
# 	age: 35
# 	position: web developer

#**kwargs для передачи переменного количества именованных аргументов.
# def names(**data):
#     print(("\n Данные пользователя:", type(data)))
#     for key, value in data.items(): #внутри функции пройтись циклом по словарю, чтобы вывести его содержимое
#         print("{} is {}".format(key, value))
# names(name = "Max", last_name = "Plank", age = 164, position = "theoretical_physicist")

# 4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список, содержащий только
#      положительные числа
# my_list = [20, -3, 15, 2, -1, -21]
# positives_only = (list(filter(lambda x: x > 0, my_list))) #решено
# print(positives_only)

# 4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке
# print(list(map(lambda a, b, c: a*b*c, positives_only)))

# import functools
# print (functools.reduce(lambda a, b: a * b, positives_only)) #решено

# 4.5. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления.
#      Примените эти функции в качестве методов в другом файле.

# from my_calc import *
#
# print(squaring(3))
# print(prod(10, 5))
# print(sum_it(25, 25))
# print(division(21, 0))

# l_programming import*

# arr1 = [6, 5, 4, 3, 2]
# arr2 = [7, 8, 9, 10, 11, 12]
# def sum_arrs2(arr0))
# # from 4.1_functiona1, arr2):
#     print(arr1)
#     print(arr2)
#     return sum(arr1 + arr2)

# def sum_arr3(arr1, arr2):
#     arr0 = arr1 + arr2
#     return (reduce(lambda x, y: x + y, arr0))
# sum_arr3(arr1=1, arr2=3)
# print sum_arr3(arr1, arr2)
#
# def avarage_arr(arr):
#     print(sum(arr)/len(arr) if len(arr) > 0 else 0)
# avarage_arr(arr= (1, 2, 3, 4, 5))

# Codewars:
# def hello(name):
#     return f'Hello, {name}'
# print(hello('Gray'))
#
# def string_to_number(s):
#     return(int(s))
# print(string_to_number(20))

# def make_upper_case(s):
#     return s.upper()
# print(make_upper_case('Ivan'))

# num = int(123)
# sum = 0
# while (num != 0):
#     sum = sum + num % 10
#     num = num // 10
# print("Сумма цифр числа равна: ", sum)
#
# def get_sum_of_digits(num):
#     sum = 0
#     while (num != 0):
#         sum = sum + num % 10
#         num = num // 10
#     print(int(get_sum_of_digits(123)))

# def get_sum_of_digits(num):
#     a = str(num)
#     sum = 0
#     for x in a:
#         # sum += int(x)
#         sum = sum + int(x)
#     return suma
# print(get_sum_of_digits(123))

# def switcheroo(s):
#     # x = a
#     # a = b
#     # b = x
#     return s.replace('a', 'x').replace('b', 'a').replace('x', 'b')

# print(switcheroo('ab'))

# def solve(s):
#     return s.upper()
# print(solve('Code'))

def solve(s):
    countUpper = 0
    countLower = 0
    for i in s:
        if i == i.upper():
            countUpper += 1
        else:
            countLower += 1
    if countUpper <= countLower:
        s = s.lower()
    else:
        s = s.upper()
    return s



# def reverse_string1(s): #поворот строки в обратную сторону
#     return s[::-1]
#
# print(reverse_string1('TURBO'))

# def is_triangle(a, b, c):
#     if (a == b == c) > 0 and int:
#         return ("True")
#     else:
#         print("False")
#
# print(is_triangle(3,3,3))
# 4521369741
def sum_single_digit(in_int: int) -> int:
    while in_int > 9:
        in_int = sum(map(int, str(in_int)))
    return in_int