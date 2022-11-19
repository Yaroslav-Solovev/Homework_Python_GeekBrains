# задача 3. Напишите программу, удаляющую из текста все слова, содержащие "абв".

text = "Едят ли кошкиабв мышек, едят абв ли мышкиабв кошек?"
def fun():
    words_text = text.split(' ') # Разбиваем текст на отдельные слова
    fragment = 'абв'
    new_text = []
    for word in words_text:
        if fragment not in word:
            new_text.append(word)
    print('Изначальный текст: ', text)
    print('Измененный текст: ', ' '.join(new_text))
fun()
