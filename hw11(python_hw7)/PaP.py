def open_file(file):
    with open(file, 'r', encoding = 'utf-8') as j:
        text = j.read()
        text = text.lower()
        text = text.split()
    for i in range(len(text)): 
        text[i] = text[i].strip('.,>-()/<?«»[]{}”“\|*"!:;—')
        if text[i] == '':
            text.remove('')
    return text

def word(file, userword):
    text = open_file(file)
    k = 0
    for i in range(len(text)):
        if text[i] == userword:
            k += 1
    return k

def ing_count(file):
    text = open_file(file)
    k = 0
    for i in range(len(text)):
        if text[i].endswith('ing'):
            k += 1
    return k

def res():
    userword = input('Введите слово на -ing: ')
    print('Количество слов на -ing: ' + str(ing_count(file)))
    print('Количество вашего слова в тексте: ' + str(word(file, userword)))

file = 'file.txt'
res()
