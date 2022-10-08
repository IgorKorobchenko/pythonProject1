
string = input('Enter word:')
for letter in string: #рекомандация писать название переменной (н-р letter), чтобы лучше было понятно для чего переменная
    print(letter, end="") #пишем end чтобы все вывелось в одну строку
print()
# string = input('Enter word:')
# for letter in range(len(string)): #выводит индексы введеного слова
#     print(letter, end="")

# for index in range(0, 10, 1):
#     print(index, end='')

for index in range(2, len(string), 1): #выводим индексы введенного слова со второго с шагом в 2
    if index == 3:
        print('Yes', end="")
    print(index, end='')