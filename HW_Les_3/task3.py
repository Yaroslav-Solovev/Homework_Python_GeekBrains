# Задача 3. Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def arr():
    mas = [1.1, 1.2, 3.1, 5, 10.01]
    print('Базовый список: ', mas)
    i = 0
    for i in range(5): #  из каждого элемента списка выводим дробную часть, убирая целую часть
        mas[i] = mas[i] - int(mas[i])
    result = max(mas) - min(mas)
    def truncate(result, decimals=2): # функция отсечения тысячных и т.д. от result
        multiplier = 10 ** decimals
        return int(result * multiplier) / multiplier
    print('Разница между максимальным и минимальным значением дробной части элементов: ', truncate(result))
arr()


