# Задача 2. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
import random

def fun():
    a = int(input('Введите размер списка: '))
    x = int(input('Введите начало диапазона чисел списка: '))
    y = int(input('Введите конец диапазона чисел списка: '))
    mas = []
    for _ in range(a):
        mas.append(random.randint(x, y))
    print('Заданный список: ', mas)
    res = []
    step = len(mas) - 1
    for i in range(0, len(mas), 1):
        if i < len(mas)/2:
            res.append(mas[i] * mas[step])
            step = step - 1  
    print("Произведение пар чисел списка: " + str(res))
fun()