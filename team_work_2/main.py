#функционал:
    # доб учениками
    # удалить учениками
    # выборка
        # все ученики класса
        # все отличники(хорошисты, троечники)
        # именинники месяца
        # по фио номер тел
        # вся информациипо фио
        # по фио класс руковод???

from easygui import *
import control as ctrl

lvl = 0
ctrl.load()

while True:
    if lvl == 0:
        msg = "Выберите дальнейшее действие: "
        title = "Информация об учениках школы № ?"
        choices = ['Добавить информацию об ученике', 'Удалить информацию об ученике', 'Редактировать информацию об ученике', 'Поиск информации']
        choice = choicebox(msg, title, choices)
        if choice == choices[0]:
            lvl = 1
        if choice == choices[1]:
            msg = "Введите ФИО ученика: "
            title = "Удаление информации об ученике"
            fieldNames  =  ["Фамилия","Имя Отчество"]
            del_stud = []
            del_stud = multenterbox(msg, title, fieldNames)
            if del_stud == False:
                lvl = 0
            else:
                msgbox(ctrl.del_stud(del_stud), 'Отчет')
        elif choice == choices[2]:
            lvl = 2
        elif choice == choices[3]:
            lvl = 3
        elif choice == None:
            msgbox("Работа системы завершена. До новых встреч!")
            break
    elif lvl == 1:
        msg = "Введите информацию об ученике: "
        title = "Ввод информации об ученике"
        fieldNames  =  ["Фамилия","Имя Отчество","Дата рождения","Класс","Классный руководитель","Адрес","Телефон родителя","Средняя успеваемость"]
        ent_stud = []
        ent_stud = multenterbox(msg, title, fieldNames)
        while True:
            if ent_stud == None:
                lvl = 0
                break
            errmsg = ""
            for i in range (len(fieldNames)):
                if ent_stud[i].strip() == "":
                     errmsg = errmsg + ('"%s" это обязательные поля.\n\n' % fieldNames[i])
            if errmsg == "":
                break # no problems found
            ent_stud = multenterbox(errmsg, title,  fieldNames, ent_stud)
        msgbox(ctrl.ent_stud(ent_stud), 'Отчет')
        lvl = 0
    elif lvl == 2:
        msg = "Введите ФИО ученика, чьи данные нужно редактировать: "
        title = "Редактирование данных об ученике"
        fieldNames  =  ["Фамилия","Имя Отчество"]
        ch_stud = []
        ch_stud = multenterbox(msg, title, fieldNames)
        if ch_stud == None:
            lvl = 0
        elif choices[3]:
            lvl = 10
    elif lvl == 3:
        msg = "Выберите шаблон поиска: "
        title = "Поиск информации"
        choices = ['Информация об ученике', 'Классный руководитель ученика', 'Телефон родителя', 'Ученики класса', 'Именинники месяца', 'Выборка по успеваемости']
        chois_sample = choicebox(msg, title, choices)
        if chois_sample == choices[0]:
            lvl = 4
        elif chois_sample == choices[1]:
            lvl = 5
        elif chois_sample == choices[2]:
            lvl = 6
        elif chois_sample == choices[3]:
            lvl = 7
        elif chois_sample == choices[4]:
            lvl = 8
        elif chois_sample == choices[5]:
            lvl = 9
        elif chois_sample == None:
            lvl = 0
    elif lvl == 4:
        msg = "Введите ФИО ученика: "
        title = "Информация об ученике"
        fieldNames  =  ["Фамилия","Имя Отчество"]
        sample1 = []
        sample1 = multenterbox(msg, title, fieldNames)
        if sample1 == None:
            lvl = 3
        else:
            msgbox(ctrl.search_info_stud(sample1), 'Отчет')
            lvl = 0
    elif lvl == 5:
        msg = "Введите ФИО ученика: "
        title = "Классный руководитель ученика"
        fieldNames  =  ["Фамилия","Имя Отчество"]
        sample2 = []
        sample2 = multenterbox(msg, title, fieldNames)
        if sample2 == None:
            lvl = 3
        else:
            msgbox(f'Классный руководитель - {ctrl.search_info_classroom_teacher_stud(sample2)}', 'Отчет')
            lvl = 0
    elif lvl == 6:
        msg = "Введите ФИО ученика: "
        title = "Телефон родителя"
        fieldNames  =  ["Фамилия","Имя Отчество"]
        sample3 = []
        sample3 = multenterbox(msg, title, fieldNames)
        if sample3 == None:
            lvl = 3
        else:
            msgbox(f'Телефон родителя - {ctrl.search_info_phone_perents_stud(sample3)}', 'Отчет')
            lvl = 0
    elif lvl == 7:
        msg = "Введите класс: "
        title = "Ученики класса"
        fieldNames  =  ["Класс"]
        sample4 = []
        sample4 = multenterbox(msg, title, fieldNames)
        if sample4 == None:
            lvl = 3
        else:
            msgbox(ctrl.search_info_class_stud(sample4), 'Ученики класса')
            lvl = 0
    elif lvl == 8:
        msg = "Введите месяц: "
        title = "Именинники месяца"
        fieldNames  =  ["Месяц"]
        sample5 = []
        sample5 = multenterbox(msg, title, fieldNames)
        if sample5 == None:
            lvl = 3
        else:
            msgbox(ctrl.search_info_birthday_mounth_stud(sample5[0]), 'Именнинники месяца')
            lvl = 0
    elif lvl == 9:
        msg = "Выберите категорию: "
        title = "Выборка по успеваемости"
        choices = ['Отличники', 'Хорошисты', 'Троечники']
        score = choicebox(msg, title, choices)
        if score == None:
            lvl = 3
        elif score == choices[0]:
            msgbox(ctrl.search_five_stud(), 'Отличники')
            lvl = 0
        elif score == choices[1]:
            msgbox(ctrl.search_four_stud(), 'Хорошисты')
            lvl = 0
        elif score == choices[2]:
            msgbox(ctrl.search_three_stud(), 'Троечники')
            lvl = 0
    elif lvl == 10:
        msg = "Выберите данные для редактирования: "
        title = "Редактирование данных об ученике"
        choices = ["Дата рождения","Класс","Классный руководитель","Адрес","Телефон родителя","Средняя успеваемость"]
        overwriting = multchoicebox(msg, title, choices)
        if overwriting == None:
            lvl = 0
        elif choices[3]:
            msg = "Введите информацию об ученике: "
            title = "Ввод информации об ученике"
            edit_stud = []
            edit_stud = multenterbox(msg, title, overwriting)
            if edit_stud == False:
                lvl = 2
            else:
                msgbox(ctrl.edit_stud(ch_stud,overwriting,edit_stud), 'Отчет')
                lvl = 2