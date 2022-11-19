# Задача 3. Реализуйте алгоритм перемешивания списка. Список размерностью 10 задается случайными целыми числами, 
# выводится на экран, затем перемешивается, опять выводится на экран. SHUFFLE нельзя юзать!

import random
def spisok(): # Функция задания списка размерностью 10, и заполненого случайными числами + перемешивание
    x = int(input('Введите начало диапазона чисел списка: '))
    y = int(input('Введите конец диапазона чисел списка: '))
    mas = []
    for _ in range(10):
       mas.append(random.randint(x, y))
    print('Заданный список: ', mas)

    array_len = len(mas)
    for index in range(array_len):
        swap = random.randrange(array_len - 1) # перемешивание
        swap += swap >= index
        mas[index], mas[swap] = mas[swap], mas[index]
    print('Перемешанный список: ', mas)
spisok()

