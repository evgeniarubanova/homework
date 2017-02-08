#var1

import re
def open_file():
    with open('Франция.html', 'r', encoding= 'utf-8') as j:
        text=j.read()
    return text

def search(text):
    capital = 'Столица(?:.|\n)+?([а-яА-Я]+)</a>'
    name = re.findall(capital, text)
    if name:
        with open ('note.txt', 'a',encoding = 'utf-8') as j:
            j.write(str(name[1]))
    else:
        print(text)
        with open('note.txt', 'a', encoding = 'utf-8') as j:
            j.write(text)

text = open_file()
search(text)


    
