# Урок 5. Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension
# задача 1. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random     
import os     

def input_numbers(input_text):  # Функция проверки на ошибку при вводе sum_sweet
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f'{input_text}'))
            if number > 0:
                is_OK = True
            else:
                print('Error: Введите число больше нуля.')
        except ValueError:
            print('Error: Вы ввели не число.')
    return number

player1 = input("Введите имя игрока № 1: ")
player2 = input("Введите имя игрока № 2: ")

def lottery():  # функция жеребьевки
    global number_player1
    global number_player2
    is_OK = False
    while not is_OK:
        number_player1 = random.randint(1,2)
        number_player2 = random.randint(1,2)
        if number_player1 != number_player2 and number_player2 != number_player1:
            is_OK = True
            print(f"{player1} ходит под номером: ", number_player1)
            print(f"{player2} ходит под номером: ", number_player2)
        else:
            print("Error: Ничья. Необходимо провести жеребьевку заново.")
    return number_player1
lottery()

sum_sweet = input_numbers("Введите количество конфет, лежащих на столе: ")
min_step_sweet = 1
max_step_sweet = 28

step1 = 0
step2 = 0
num_flag = lottery

def input_dat(name):  # Функция забиранния конфет со стола
    x = input_numbers(f"{name}, введите количество конфет, которое хотите взять в диапазоне от {min_step_sweet} до {max_step_sweet}: ")
    while (x < min_step_sweet or x > max_step_sweet): #and (x < sum_sweet)
        x = input_numbers(f"{name}, введите корректное количество конфет: ")
    return x

def p_print(name, x):  # Функция вывода информации о результатах по каждому ходу игрока
    print(f"Ходил {name}, он взял {x}")

def p_print2(name, step, sum_sweet): # Функция вывода информации о итогах раунда (1 ход 1 игрока и 1 ход 2 игрока)
    print(f"После окончания раунда у {name} {step} конфет. Осталось на столе {sum_sweet} конфет.")

while sum_sweet > 0: # Цикл ходов игроков
    if number_player1 < number_player2:
        if num_flag:
            x = input_dat(player1)
            step1 += x
            sum_sweet -= x
            num_flag = False
            p_print(player1, x)
        else:
            x = input_dat(player2)
            step2 += x
            sum_sweet -= x
            num_flag = True
            p_print(player2, x)
            print()
            p_print2(player1, (step1 - step1), sum_sweet)
            p_print2(player2, (step2 + step1), sum_sweet)
            print()
            if step1 == sum_sweet: # проверка на предварительный выйгрыш
                print(f"Выиграл {player1} как забравший все конфеты.")
                os._exit
            elif step2 == sum_sweet:
                print(f"Выиграл {player2} как забравший все конфеты.")
                os._exit
            else:
                if step1 > step2:
                    print(f"На основании подчета набранных каждым игроком конфет выиграл {player1}.")
                    os._exit
                elif step2 == sum_sweet:
                    print(f"На основании подчета набранных каждым игроком конфет выиграл {player2}.")
                    os._exit
            lottery()
    else:
        if num_flag:
            x = input_dat(player2)
            step2 += x
            sum_sweet -= x
            num_flag = False
            p_print(player2, x)
        else:
            x = input_dat(player1)
            step1 += x
            sum_sweet -= x
            num_flag = True
            p_print(player1, x)
            print()
            p_print2(player2, (step2 - step2), sum_sweet)
            p_print2(player1, (step1 + step2), sum_sweet)
            print()
            if step1 == sum_sweet: # проверка на предварительный выйгрыш
                print(f"Выиграл {player1} как забравший все конфеты.")
                os._exit
            elif step2 == sum_sweet:
                print(f"Выиграл {player2} как забравший все конфеты.")
                os._exit
            else:
                if step1 > step2:
                    print(f"На основании подчета набранных каждым игроком конфет выиграл {player1}.")
                    os._exit
                elif step2 == sum_sweet:
                    print(f"На основании подчета набранных каждым игроком конфет выиграл {player2}.")
                    os._exit
            lottery()

if num_flag:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")
