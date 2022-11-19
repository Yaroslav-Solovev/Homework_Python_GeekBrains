# задача 4. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

def InputNumbers(inputText): # Функция проверки на ошибку при вводе
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f'{inputText}'))
            if number != 0:
                is_OK = True
            else: print('Error. Деление на ноль.')
        except ValueError:
            print('Error: Вы ввели не число.')
    return number

from math import lcm

a = InputNumbers('Введите число a: ')
b = InputNumbers('Введите число b: ')

def get_lcm(a, b): # функция нахождения НОК
    return lcm(a, b)
print(get_lcm(a, b))