#var1

import re

def open_file(file):
    with open(file, 'r', encoding = 'utf-8') as j:
        text = j.read()
    text = re.split('\.|\?|!|\.\.\.|\?!', text)
    text = [re.sub(',|>|«|»|"|[|]|{|}|<|\*|:|;|—|\'', '', i) for i in text]
    return text

def wsplit(file):
    text = open_file(file)
    text = [i.split() for i in text]
    return text

def search(file):
    text = wsplit(file)
    txt = [l for i in text for l in i]
    words = [len(i) for i in txt]
    for i in range(len(txt)):
        if words[i]>7:
            print(txt[i] + '{:->10}'.format(words[i]))

file = input('Введите название файла: ')
search(file)
            
    
