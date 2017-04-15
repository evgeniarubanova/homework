# var 1

import re
import os
import shutil

def prog():
    number_name = '[0-9]'
    folders = os.listdir('.')
    l = 0
    for i in folders:
        if os.path.isdir(i) and re.search(number_name, i):
            l += 1
    print('Кол-во папок с цифрой в названии = ' + str(l))

def names():
    arr_names = []
    name = r'.*\.'
    names = os.listdir('.')
    for i in names:
        if os.path.isfile(i)and re.search(name, i):
            file = re.search(name, i).group(0).strip('.')
            if file not in arr_names:
                arr_names.append(file)
                print(file)
        elif os.path.isdir(i):
            arr_names.append(i)
            print(i)

prog()
names()            
