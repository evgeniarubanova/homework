
#была изменена кодировка всех файлов на utf-8

import re
import os


def files():
    for i in os.listdir('.'):
        reg = '<se>'
        if i.endswith('.xhtml'):
            m = []
            with open(os.path.join('.', i), 'r', encoding = 'utf-8') as j:
                text = j.read()
    return text


def number():
    for i in os.listdir('.'):
        reg = '<se>'
        if i.endswith('.xhtml'):
            m = []
            with open(os.path.join('.', i), 'r', encoding = 'utf-8') as j:
                text = j.read()
            for j in re.findall(reg, text):
                m.append(j)
            with open('file.txt', 'a', encoding = 'utf-8') as l:
                l.write(i+'\t'+str(len(m)) + '\n')
    
def table():
    for f in os.listdir('.'):
        with open(os.path.join('.', f), 'r', encoding = 'utf-8') as k:
            text = k.read()
        reg = '<meta content="(\w*)" name="author">'
        for k in re.findall(reg, text):
            reg2 = '<meta content="(\w*)" name="header">'
            if re.search(reg2, text):
                with open('table.csv', 'a', encoding = 'utf-8') as n:
                    n.write(f+','+k+','+re.search(reg2, text).group(1)+'\n')

files()
number()
table()
