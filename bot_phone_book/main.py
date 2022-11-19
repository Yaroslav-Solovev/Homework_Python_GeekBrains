import telebot
from telebot import types
import json

API_TOKEN='Ваш TOKEN'
bot = telebot.TeleBot(API_TOKEN)

print("Bot is start")

def save():
    with open("book.json","w",encoding="utf-8") as fh:
        fh.write(json.dumps(phone_book,ensure_ascii=False))
    print("Файл book.json обновлен.")

def load():
    global phone_book
    with open("book.json","r",encoding="utf-8") as fh:
        phone_book=json.load(fh)
    print("Телефонная книга успешно загружена")

def search_contact(phone_num: int):
    global phone_book
    with open("book.json","r",encoding="utf-8") as fh:
        for key,value in phone_book.items():
            for k in value:
                if k==phone_num:
                    return key

@bot.message_handler(commands=['start'])
def startMessage(message):
    load()
    key = {}
    keyboard_1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    key[0] = types.KeyboardButton("Посмотреть все контакты")
    key[1] = types.KeyboardButton("Найти контакт")
    key[2] = types.KeyboardButton("Добавить контакт")
    key[3] = types.KeyboardButton("Удалить контакт")
    keyboard_1.row(key[0], key[1])
    keyboard_1.row(key[2], key[3])

    name = message.from_user.first_name
    bot.send_message(message.chat.id,f"Привет, {name}! Я Teлефонный бот, у меня сохранены все твои контакты. Чем тебе помочь?", parse_mode='html', reply_markup=keyboard_1)

@bot.message_handler(func=lambda message: True)
def menu(message):
    if message.chat.type == 'private':
        if message.text == "Посмотреть все контакты":
            for key in phone_book: 
                bot.send_message(message.chat.id, f"{key}: {str(phone_book[key]).replace('[', '').replace(']', '')}")
        elif message.text == "Найти контакт":
            markup_1 = types.InlineKeyboardMarkup(row_width=1)
            but1 = types.InlineKeyboardButton("Найти по фамилии", callback_data='text1')
            but2 = types.InlineKeyboardButton("Найти по номеру телефона", callback_data='text2')
            markup_1.add(but1,but2)
            bot.send_message(chat_id=message.chat.id, text="Выбери, каким способом искать:", reply_markup=markup_1)
        elif message.text == "Добавить контакт":
            markup_2 = types.InlineKeyboardMarkup(row_width=1)
            but1 = types.InlineKeyboardButton("Добавить данные", callback_data='new')
            markup_2.add(but1)
            bot.send_message(chat_id=message.chat.id, text="Введите данные нового контакта:", reply_markup=markup_2)
        elif message.text == "Удалить контакт":
            markup_3 = types.InlineKeyboardMarkup(row_width=1)
            but1 = types.InlineKeyboardButton("Удалить все данные контакта", callback_data='del')
            but2 = types.InlineKeyboardButton("Удалить номер телефона контакта", callback_data='del_num')
            markup_3.add(but1,but2)
            bot.send_message(chat_id=message.chat.id, text="Выберите какие данные нужно удалить:", reply_markup=markup_3)
        
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
            if call.data == 'text1':
                msg = bot.send_message(call.message.chat.id, "Введите фамилию:")
                bot.register_next_step_handler(msg, show_name)
            elif call.data == 'text2':
                msg = bot.send_message(call.message.chat.id, "Введите номер телефона:")
                bot.register_next_step_handler(msg, show_number)
            elif call.data == 'new':
                msg = bot.send_message(call.message.chat.id, "Укажите фамилию и номера телефонов через пробел!")
                bot.register_next_step_handler(msg, add_new_contact)
            elif call.data == 'del':
                msg = bot.send_message(call.message.chat.id, "Укажите фамилию контакта:")
                bot.register_next_step_handler(msg, del_contact)
            elif call.data == 'del_num':
                msg = bot.send_message(call.message.chat.id, "Укажите номер контакта:")
                bot.register_next_step_handler(msg, del_num_contact)

def show_name(message):
    global phone_book
    quest = message.text
    bot.send_message(message.chat.id, f'{quest}: {phone_book.get(quest)}')
    if phone_book.get(quest)==None:
        bot.send_message(message.chat.id, 'Такого контакта нет в телефонном справочнике!')

def show_number(message):
    quest = int(message.text)
    key = search_contact(quest)
    bot.send_message(message.chat.id, f'{key}: {quest}')
    if key==None:
        bot.send_message(message.chat.id, 'Такого номера нет в телефонном справочнике!')

def add_new_contact(message):
    global phone_book
    quest = message.text.split()
    if quest == [] or len(quest) < 2:
        bot.send_message(message.chat.id, 'Информация введена не полностью. Попробуйте еще раз!')
    else:
        if len(quest) > 2:
            phone_book[quest[0]] = []
            for i in range(len(quest)):
                if i>0:
                    phone_book[quest[0]].append(int(quest[i]))
            save()
            bot.send_message(message.chat.id, 'Контакт добавлен в телефонную книгу!')

def del_contact(message):
    global phone_book
    quest = message.text
    del phone_book[quest]
    save()
    bot.send_message(message.chat.id, 'Запись удалена!')

def del_num_contact(message):
    global phone_book
    quest = int(message.text)
    for key, value in phone_book.items():
        for k in value:
            if k==quest:
                phone_book[key].remove(k)
    save()
    bot.send_message(message.chat.id, 'Номер телефона удалён!')
    
bot.polling()

























# @bot.message_handler(commands=['start'])
# def start_message(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     btn1 = types.KeyboardButton("Список контактов")
#     btn2 = types.KeyboardButton("Поиск")
#     btn3 = types.KeyboardButton("Добавить контакт")
#     btn4 = types.KeyboardButton("Изменить контакт")
#     btn5 = types.KeyboardButton("Удалить контакт")
#     markup.add(btn1, btn2, btn3, btn4, btn5)
#     if message.text == "/start":
#         load()
#         bot.send_message(message.chat.id, 
#         "Телебот приветсвует, {0.first_name}! Телефонная книга загружена!)".format(message.from_user, bot.get_me()), 
#         parse_mode='html', reply_markup=markup)


# @bot.message_handler(content_types=['text'])
# def func(message):
#     if(message.text == "Список контактов"):
#         for i in range(len(phone_book)):
#             item[i] = types.InlineKeyboardButton(phone_book[i], callback_data=str(i))
#             print(item[i])
#             print()
#         bot.send_message(message.chat.id, f'{phone_book}')
#     # elif(message.text == "Поиск"):
#     #     bot.send_message(message.chat.id, text="Введите Фамилию")
#     #     for i in range(len(phone_book)):
#     #         for j in range(len(phone_book[i])):
#     #             if phone_book[i][j] == text:

#     #         item[i] = types.InlineKeyboardButton(phone_book[i], callback_data=str(i))
#     #         print(item[i])
#     #         print()
#     #     bot.send_message(message.chat.id, f'{phone_book}')
    
#     elif(message.text == "Добавить контакт"):
#         bot.send_message(message.chat.id, text="Введите Фамилию и номер телевона через пробел")
        
#         bot.send_message(message.chat.id, "У меня нет имени..")
    
#     elif message.text == "Что я могу?":
#         bot.send_message(message.chat.id, text="Поздороваться с читателями")
    
#     elif (message.text == "Вернуться в главное меню"):
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#         button1 = types.KeyboardButton("👋 Поздороваться")
#         button2 = types.KeyboardButton("❓ Задать вопрос")
#         markup.add(button1, button2)
#         bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
#     else:
#         bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..")


# # @bot.message_handler(commands=['start'])
# # def start_message(message):
# #     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
# #     item[0] = types.KeyboardButton("Список контактов.")
# #     item[1] = types.KeyboardButton("Поиск.")
# #     item[2] = types.KeyboardButton("Добавить контакт.")
# #     item[3] = types.KeyboardButton("Изменить контакт.")
# #     item[4] = types.KeyboardButton("Удалить контакт.")
# #     markup.add(item[0])
# #     markup.add(item[1])
# #     markup.add(item[2])
# #     markup.add(item[3])
# #     markup.add(item[4])
# #     if message.text == "/start":
# #         load()
# #         bot.send_message(message.chat.id, 
# #         "Телебот приветсвует, {0.first_name}! Телефонная книга загружена!)".format(message.from_user, bot.get_me()), 
# #         parse_mode='html', reply_markup=markup)




# # # @bot.message_handler(content_types=["text"])
# # # def any_msg(message):
# # #     keyboard = types.InlineKeyboardMarkup()
# # #     callback_button = types.InlineKeyboardButton(text="Нажми меня", callback_data="test")
# # #     keyboard.add(callback_button)
# # #     bot.send_message(message.chat.id, "Я – сообщение из обычного режима", reply_markup=keyboard)


# @bot.message_handler(content_types=['text'])
# def mess(message):
#     if message.chat.type == 'private':
#         if message.text == "Телефонная книга.":
#             global gameIsStart
#             gameIsStart = True
#         else:
#             bot.send_message(message.chat.id, "Я не знаю таких слов.")
#     if gameIsStart == True:
#         item = {}
#         global markup
#         markup = types.InlineKeyboardMarkup()
#         i = 0
#         for i in range(len(phone_book)):
#             item[i] = types.InlineKeyboardButton(phone_book[i], callback_data=str(i))
#             print(item[i])
#             print()
#         bot.send_message(message.chat.id, f'{phone_book}')


# @bot.message_handler(commands=["Список контактов."])
# def show_all(message):
#     bot.send_message(message.chat.id,"Вот список контактов")
#     bot.send_message(message.chat.id, f'{phone_book}')
#     print(phone_book)

# # @bot.message_handler(commands=['create'])
# # def create(message):
# #     global phone_book
# #     quest = message.text.split()[1:]
# #     print(quest)
# #     if quest == [] or len(quest) < 2:
# #         bot.send_message(message.chat.id, 'Информация введена не полностью. Попробуйте еще раз.')
# #     else:
# #         if len(quest) > 2:
# #             while len(quest) > 2:
# #                 quest[-2] = quest[-2] + ', ' + quest[-1]
# #                 quest.pop()
# #         phone_book[quest[0]] = quest[1]
# #         save()
# #         bot.send_message(message.chat.id,"Контакт добавлен.")

# # @bot.message_handler(commands=['del'])
# # def create(message):
# #     global phone_book
# #     quest = message.text.split()[1:]
# #     del phone_book[quest[0]]
# #     bot.send_message(message.chat.id, 'Запись удалена.')
# #     save()    

# # @bot.message_handler(commands=['show'])
# # def create(message):
# #     global phone_book
# #     quest = message.text.split()[1:]
# #     bot.send_message(message.chat.id, f'{quest[0]}: {phone_book.get(quest[0])}')

# # @bot.message_handler(commands=['help'])
# # def create(message):
# #     bot.send_message(message.chat.id, '/all - отображение всех записей\n/create - добавление записи: Фамилия телефон(ы)\n/del - удаление записи по Фамилии\n/show - отображение записи по Фамилии')

# bot.polling()



# #https://stepik.org/course/63054?search=1409909486


# # phone_book = [{"Surname": "Петров", "Name": "Иван", "Patronymic": "Петрович", "Number": [435678, 456908], "City": "Moscow"}]
