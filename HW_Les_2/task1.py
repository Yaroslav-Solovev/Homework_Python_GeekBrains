# Задача 1. Напишите программу, которая принимает на вход вещественное 
# или целое число и показывает сумму его цифр. Через строку нельзя решать.

# *Пример:*

# - 6782 -> 23
# - 0,56 -> 11

number = input('Введите дробное число либо целое со знаком <.>: ')
x = number.split('.') 
a = int(x[0]) # целая часть
b = int(x[1]) # дробная часть

sum = 0
while (a != 0): 
    sum += a % 10
    a = a // 10
while (b != 0):
    sum += b % 10
    b = b // 10
print('Сумма цифр введенного числа равна: ', sum)