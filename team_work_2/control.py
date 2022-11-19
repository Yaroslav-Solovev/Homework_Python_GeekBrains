import json

data_base = []

def load():
    global data_base
    with open("student_data_base.json", "r", encoding="utf-8") as fh:
        data_base = json.load(fh)
    print("База учеников успешно была загружена")

def save():
    with open("student_data_base.json", "w", encoding="utf-8") as fh:
        fh.write(json.dumps(data_base,ensure_ascii=False))
    print("Наша база была успешно сохранена в файле student_data_base.json")

def ent_stud(list):
    ret_msg = f"Инфомация: {list} добавлена в систему."
    flag = True
    for i in range(len(data_base)):
        if data_base[i][0] == list[0] and data_base[i][1] == list[1]:
           ret_msg = f"Ученик {list[0]} {list[1]} уже есть в системе"
           flag = False
           break
    if flag:
        with open("student_data_base.json", "w", encoding="utf-8") as fh:
            data_base.append(list)
            fh.write(json.dumps(data_base,ensure_ascii=False))
    return ret_msg

def dict(text):
    if text == "Дата рождения":
        return 2
    elif text == "Класс":
        return 3
    elif text == "Классный руководитель":
        return 4
    elif text == "Адрес":
        return 5
    elif text == "Телефон родителя":
        return 6
    elif text == "Средняя успеваемость":
        return 7

def del_stud(list1):
    ret_msg = "Ученик не найден в системе."
    for i in range(len(data_base)):
        if data_base[i][0] == list1[0] and data_base[i][1] == list1[1]:
            data_base.pop(i)
            save()
            ret_msg = "Инофрмация об ученике удалена из системы."
    return ret_msg

def edit_stud(list1, list2, list3):
    ret_msg = "Ученик не найден в системе."
    for i in range(len(data_base)):
        if data_base[i][0] == list1[0] and data_base[i][1] == list1[1]:
            for j in range(len(list2)):
                data_base[i][dict(list2[j])] = list3[j]
            save()
            ret_msg = "Информация изменена."
    return ret_msg

def search_info_stud(list1): # для lvl == 4:
    ret_msg = "Ученик не найден в системе."
    for i in range(len(data_base)):
        if data_base[i][0] == list1[0] and (data_base[i][1] == list1[1] or list1[1] == ''):
            ret_msg = data_base[i]
    return ret_msg

def search_info_classroom_teacher_stud(list1): # для lvl == 5:
    ret_msg = "Ученик не найден в системе."
    for i in range(len(data_base)):
        if data_base[i][0] == list1[0] and (data_base[i][1] == list1[1] or list1[1] == ''):
            ret_msg = data_base[i][4]
    return ret_msg

def search_info_phone_perents_stud(list1): # для lvl == 6:
    ret_msg = "Ученик не найден в системе."
    for i in range(len(data_base)):
        if data_base[i][0] == list1[0] and (data_base[i][1] == list1[1] or list1[1] == ''):
            ret_msg = data_base[i][6]
    return ret_msg

def search_info_class_stud(group): # для lvl == 7:
    ret_msg = "Класс не найден в системе."
    all_list = []
    for i in range(len(data_base)):
        if group[0] == data_base[i][3]:
            class_list = data_base[i][0] + " " + data_base[i][1]
            all_list.append(class_list)
    if all_list != []:
        ret_msg = all_list             
    return ret_msg

def search_info_birthday_mounth_stud(list1): # для lvl == 8:
    ret_msg = "Такого месяца не существует."
    mounth = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]
    if list1.isdigit() and (0 < int(list1) < 13):
        list1 = int(list1)
    elif list1.lower() in mounth:
        list1 = mounth.index(list1) + 1
    else:
        return ret_msg
    birthday = []
    for i in range(len(data_base)):
        data_birthday_stud = data_base[i][2]
        if int(data_birthday_stud[3:5]) == list1:
            print(data_base[i][0]+' '+data_base[i][1]+' '+data_base[i][2])
            birthday.append(data_base[i][0]+' '+data_base[i][1]+' '+data_base[i][2])
    if birthday == []:
        ret_msg = "Именинников в этом месяце нет"
    else:
        ret_msg = birthday
    return ret_msg

def search_five_stud(): # для lvl == 9 отличники:
    ret_msg = []
    for i in range(len(data_base)):
        if data_base[i][7] == "5":
            ret_msg.append(data_base[i][0]+' '+data_base[i][1]+' '+data_base[i][3])
    return ret_msg

def search_four_stud(): # для lvl == 9 хорошисты:
    ret_msg = []
    for i in range(len(data_base)):
        if data_base[i][7] == "4":
            ret_msg.append(data_base[i][0]+' '+data_base[i][1]+' '+data_base[i][3])
    return ret_msg

def search_three_stud(): # для lvl == 9 троечники:
    ret_msg = []
    for i in range(len(data_base)):
        if data_base[i][7] == "3":
            ret_msg.append(data_base[i][0]+' '+data_base[i][1]+' '+data_base[i][3])
    return ret_msg