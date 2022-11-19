# НЕЛЬЗЯ ИСПОЛЬЗОВАТЬ EVAL! максимум для тестирования
# Задача 1. Создайте программу для игры в "Крестики-нолики".
 
matrix = list(range(1,10))
def print_matrix(matrix):
    for i in range(3): 
        print(matrix[0+i*3], matrix[1+i*3], matrix[2+i*3])

def take_input(player_move): # Функция определения и произведения ходов игроков
    valid = False
    while not valid:
        player_answer = input("Твой ход игрок под номером " + player_move +" : ")
        try:
            player_answer = int(player_answer)
        except:
            print("Error: Вы ввели не число.")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if(str(matrix[player_answer-1]) not in "XO"):
                matrix[player_answer-1] = player_move
                valid = True
            else:
                print("Error: Эта клетка уже занята. Повтори ход.")
        else:
            print("error: Введите число от 1 до 9.")

def check_win(matrix): # Функция, определяющая выйгрышные позиции
    win_position = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
    for evry in win_position:
        if matrix[evry[0]] == matrix[evry[1]] == matrix[evry[2]]:
            return matrix[evry[0]]
    return False

def main(matrix): # Функция подчета и определения кто выйграл
    step = 0
    win = False
    while not win:
        print_matrix(matrix)
        if step % 2 == 0:
           take_input("X")
        else:
           take_input("O")
        step += 1
        if step > 4:
           name = check_win(matrix)
           if name:
              print("Игрок под номером ", name, " выиграл.")
              win = True
              break
        if step == 9:
            print("Ничья.")
            break
    print_matrix(matrix)
main(matrix)
