# задача 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.

# *Пример:*

# - 6 -> да
# - 7 -> да
# - 1 -> нет

# Функция ввода числа с проверкой на ошибки
def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Error: Вы ввели не число.")
    return number

# Функция определяющая какому дню соотвествует та или иная цифра
def NumberHoliday(num):
    if num == 1:
        print('(Понедельник)')
    elif num == 2:
        print('(Вторник)')
    elif num == 3:
        print('(Среда)')  
    elif num == 4:
        print('(Четверг)')
    elif num == 5:
        print('(Пятница)')
    elif num == 6:
        print('(Суббота)')
    elif num == 7:
        print('(Воскресенье)')

# Функция проверки - является ли введенное число выходным днем или нет
def checkNumber(num):
    if num == 6 or num == 7:
        print('Веденное число ', num, ' является выходным днем недели.')
    elif num < 1 or num > 7:
        print('Error: Такого дня недели не существует. Введите значение заново.')
    else:
        print('Веденное число ', num, ' не является выходным днем недели.')

num = InputNumbers('Введите число n: ') 
NumberHoliday(num)
checkNumber(num)