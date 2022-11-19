# задача 1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# для проверки
# 50 = 5 * 5 * 2
# 10 = 5 * 2

def InputNumbers(inputText): # Функция проверки на ошибку при вводе
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f'{inputText}'))
            if number > 0:
              is_OK = True
            else:
              print('Введите число больше 0.')
        except ValueError:
            print('Error: Вы ввели не число.')
    return number

def fun(): # Функция составления списка простых множителей числа N
    n = InputNumbers('Введите натуральное число N: ')
    arr_prostonum = []
    prostonum = 2
    if n == 1: print([1])
    else:
        while n > 1:
            if n % prostonum == 0:
                arr_prostonum.append(prostonum)
                n = n/prostonum
            else:
                prostonum += 1
        print(arr_prostonum)
fun()