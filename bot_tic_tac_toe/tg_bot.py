import telebot
import random
from telebot import types

API_TOKEN = 'Ваш TOKEN'
bot = telebot.TeleBot(API_TOKEN)

item = {}
gameIsStart = False
gameGround = [" ", " ", " ",
              " ", " ", " ",
              " ", " ", " ", ]

CrossesOrToe = ["0", "X"]
playerSymbol = CrossesOrToe[random.randint(0, 1)]

botSymbol = ""
if (playerSymbol == "0"):
    botSymbol = "X"
else:
    botSymbol = "0"

print("Bot is start")

winbool = False
losebool = False

def clear():
    global gameGround
    gameGround = [" ", " ", " ",
                  " ", " ", " ",
                  " ", " ", " "]

def win(cell_1, cell_2, cell_3):
    if cell_1 == playerSymbol and cell_2 == playerSymbol and cell_3 == playerSymbol:
        print("Your win!")
        global winbool
        winbool = True

def lose(cell_1, cell_2, cell_3):
    if cell_1 == botSymbol and cell_2 == botSymbol and cell_3 == botSymbol:
        print("Sorry. Your lose)")
        global losebool
        losebool = True

def defend(cell_1, cell_2, posDef):
    if cell_1 == playerSymbol and cell_2 == playerSymbol:
        posDef = botSymbol

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item[0] = types.KeyboardButton("Крестики-нолики.")
    markup.add(item[0])
    if message.text == "/start":
        bot.send_message(message.chat.id, 
        "Привет, {0.first_name}!, давай сыграем!)".format(message.from_user, bot.get_me()), 
        parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def mess(message):
    if message.chat.type == 'private':
        if message.text == "Крестики-нолики.":
            global gameIsStart
            gameIsStart = True
        else:
            bot.send_message(message.chat.id, "Я не знаю таких слов.")
    if gameIsStart == True:
        item = {}
        bot.send_message(message.chat.id, "Игра началась!")
        global markup
        markup = types.InlineKeyboardMarkup(row_width=3)
        i = 0
        for i in range(9):
            item[i] = types.InlineKeyboardButton(gameGround[i], callback_data=str(i))
        markup.row(item[0], item[1], item[2])
        markup.row(item[3], item[4], item[5])
        markup.row(item[6], item[7], item[8])
        bot.send_message(message.chat.id, "Выбери клетку.", reply_markup = markup)

@bot.callback_query_handler(func=lambda call: True)
def callbackInline(call):
    if (call.message):
        randomCell = random.randint(0, 8)
        if gameGround[randomCell] == playerSymbol:
            randomCell = random.randint(0, 8)
        if gameGround[randomCell] == botSymbol:
            randomCell = random.randint(0, 8)
        if gameGround[randomCell] == " ":
            gameGround[randomCell] = botSymbol
        for i in range(9):
            if call.data == str(i):
                if (gameGround[i] == " "):
                    gameGround[i] = playerSymbol
    
            win(gameGround[0], gameGround[1], gameGround[2])
            win(gameGround[0], gameGround[4], gameGround[8])
            win(gameGround[6], gameGround[4], gameGround[2])
            win(gameGround[6], gameGround[7], gameGround[8])
            win(gameGround[0], gameGround[3], gameGround[6])
            lose(gameGround[0], gameGround[1], gameGround[2])
            lose(gameGround[0], gameGround[4], gameGround[8])
            lose(gameGround[6], gameGround[4], gameGround[2])
            lose(gameGround[6], gameGround[7], gameGround[8])
            lose(gameGround[0], gameGround[3], gameGround[6])

            item[i] = types.InlineKeyboardButton(gameGround[i], callback_data=str(i))

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Крестики-нолики", reply_markup=None)

        global markup
        markup.row(item[0], item[1], item[2])
        markup.row(item[3], item[4], item[5])
        markup.row(item[6], item[7], item[8])

        bot.send_message(call.message.chat.id, "Выбери клетку", reply_markup=markup)
        global gameIsStart
        global winbool
        global losebool
        if winbool:
            print()
            clear()
            bot.send_message(call.message.chat.id, "Я проиграл :(")
            winbool = False
            gameIsStart = False
        if losebool:
            print()
            clear()
            bot.send_message(call.message.chat.id, "Я выиграл!")
            losebool = False
            gameIsStart = False

bot.polling(none_stop=True)