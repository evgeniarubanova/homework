import re

def open_file():
    with open('Комар.html', 'r', encoding = 'utf-8') as j:
        text = j.read()
    return text

def replace():
    text = open_file()
    r = re.sub(r'\bКомар\w?\w?\w?', r'Слон', text)
    text = re.sub(r'\bкомар\w?\w?\w?', r'слон', r)
    return text

def writedown():
    text = replace()
    with open ('note.txt', 'a', encoding = 'utf-8') as j:
        j.write(text)

replace()   
writedown()

