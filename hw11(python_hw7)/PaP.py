def file(PaP):
    with open(PaP, 'r', encoding = 'utf-8') as f:
        text = f.read()
        text = text.lower()
        text = text.split()
        for i in range(len(text)): 
            text[i] = text[i].strip('”“".,>«»@&#+=[]{}\|/<*!:;—()-?')
            if text[i] == ' ':
                text.remove('')
    return(text)

def ing_numb(PaP):
    k = 0
    text = file(PaP)
    for i in range(len(text)):
        if text[i].endswith('ing'):
            k +=1
    return k

def ing_pers(PaP, ing_form):
    k = 0
    text = file(PaP)
    for i in range(len(text)):
        if text[i] == ing_form:
            k +=1
    return k

def print_form():
    PaP = input('Введите название файла: ')
    ing_form = input('Введите форму на -ing: ')
    print('Кол-во слоформ на -ing в тексте: ' + str(ing_numb(PaP)))
    print('Кол-во слова ' + ing_form + ': ' + str(ing_pers(PaP, ing_form)))

print_form()
