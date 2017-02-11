def open_file(file):
    with open(file, 'r', encoding = 'utf-8') as j:
        text = j.read()
        text = text.lower()
        text = text.split()
    for i in range(len(text)): 
        text[i] = text[i].strip('”“".,>«»@&#+=[]{}\|/<*!:;—()-?')
        if text[i] == ' ':
            text.remove('')
    return(text)

def ing_count(file):
    text = open_file(file)
    k = 0
    for i in range(len(text)):
        if text[i].endswith('ing'):
            k += 1
    return k


def ing_word(file, ing_form):
    text = open_file(file)
    k = 0
    for i in range(len(text)):
        if text[i] == ing_form:
            k += 1
    return k

def print_res():
    file = input('Введите название файла: ')
    ing_form = input('Введите слово на -ing: ')
    print('Количество слов на -ing в тексте: ' + str(ing_count(file)))
    print('Количество слова ' + ing_form + ': ' + str(ing_word(file, ing_form)))

print_res()
