# задача 4 HARD необязательная Напишите простой калькулятор, который считывает с пользовательского 
# ввода три строки: первое число, второе число и операцию, после чего применяет операцию 
# к введённым числам ("первое число" "операция" "второе число") и выводит результат на экран.

# Поддерживаемые операции: +, -, /, *, mod, pow, div, где
# mod — это взятие остатка от деления,
# pow — возведение в степень,
# div — целочисленное деление.

# Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".

# Обратите внимание, что на вход программе приходят вещественные числа.

# Sample Input 1:
# 5.0
# 0.0
# mod
# Sample Output 1:
# Деление на 0!

# Sample Input 2:
# -12.0
# -8.0
# *
# Sample Output 2:
# 96.0

# Sample Input 3:
# 5.0
# 10.0
# /
# Sample Output 3:
# 0.5

# Функция ввода числа A с проверкой на ошибки
def InputNumbersA(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = float(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Error: Вы ввели не число.")
    return number

# Функция ввода числа B с проверкой на ошибки
def InputNumbersB(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = float(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Error: Вы ввели не число.")
    return number

# Функция калькулятора
def Сalculator(a, b, c):
    if c == '+':
        print(a+b)
    elif c == '-':
        print(a-b)
    elif c == '*':
        print(a*b)
    elif c == '/' and b == 0:
        print("Деление на 0!")
    elif c == '/' and b != 0:
        print(a/b)
    elif c == 'mod' and b == 0:
        print('Деление на 0!')
    elif c == 'mod' and b != 0:
        print(a%b)
    elif c == 'pow':
        print(a**b)
    elif c == 'div' and b == 0:
        print('Деление на 0!')
    elif c == 'div' and b != 0:
        print(a//b)

a = InputNumbersA('Введите первую цифру: ')
b = InputNumbersB('Введите вторую цифру: ')
c = str (input('Введите знак операции: '))
Сalculator(a, b, c)
