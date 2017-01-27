def func(file):
    with open(file, "r", encoding = "utf-8") as j:
        text = j.read()
        text = text.lower()
        text = text.split()
    for i in range(len(text)): 
        text[i] = text[i].strip('”“".,>«»@&#+=[]{}\\|/<*!:;—()\'-?')
        if text[i] == ' ':
            text.remove('')
    return (text)

import re
regex = r'\bоткр(о((ют?)|е(шь|т|м|те)|й(те)?)|ы((л([аои]?)|ть|т(ы(е|ми?|х|й)?)|ая?|ую|о(го|му?|е|й|ю)?)|в|вш(и([ймех]?|ми)?|е(го|му?|й|е)|ая|ую|ею)))(с[яь])?\b'

def recherche():
    allforms = []
    text = func(file)
    for i in range(len(text)):
        if re.search(regex, text[i]) != None:
            if text[i] not in allforms:
                allforms.append(text[i])
    print("Формы глагола 'открыть' в тексте: " + ",".join(allforms) + ".")

file = input('Введите название файла: ')
recherche()
