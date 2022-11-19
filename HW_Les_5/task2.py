# задача 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.

file1 = open('file.txt', 'r')
file1 = file1.read()

def encode_message(message): # Модуль сжатия данных
    encoded_string = ""
    i = 0
    while (i <= len(message)-1):
        count = 1
        ch = message[i]
        j = i
        while (j < len(message)-1): 
            if (message[j] == message[j + 1]): 
                count = count + 1
                j = j + 1
            else: 
                break
        encoded_string = encoded_string + str(count) + ch
        i = j + 1
    return encoded_string

def decode(our_message): # Модуль восстановления данных
    decoded_message = ""
    i = 0
    j = 0
    while (i <= len(our_message) - 1):
        run_count = int(our_message[i])
        run_word = our_message[i + 1]
        for j in range(run_count):
            decoded_message = decoded_message+run_word
            j = j + 1
        i = i + 2
    return decoded_message

def display(): # Модуль вывода и перезаписи данных в другой файл
    our_message = file1
    encoded_mes=encode_message(our_message)
    decoded_mes=decode(encoded_mes)
    data = open('newfile.txt', 'a')
    data.writelines("Encoded string: ")
    data.writelines(encoded_mes)
    data.writelines("; Decoded string: ")
    data.writelines(decoded_mes)
    data.close()
    exit()
display()
