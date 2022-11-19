# задача 2 . Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

def InputNumbers(inputText): # Функция проверки на ошибку при вводе
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f'{inputText}'))
            is_OK = True
        except ValueError:
            print('Error: Вы ввели не число.')
    return number

def arr(): #  Функция формирование начального списка и вывода списка неповторяющихся элементов
    a = InputNumbers('Введите размер списка: ')
    mas = []
    for i in range(a):
         mas.append(InputNumbers('Введите элемент: '))
    print('Заданный список: ', mas)
    res = []
    for i in mas:
        if mas.count(i) == 1:
            res.append(i)
    print('Список неповторяющихся элементов исходной последовательности: ', res)
arr()