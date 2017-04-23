# var 1

import re
import os

def depth(path):
    n = ''
    for root, dirs, files in os.walk(path, topdown = False):
        for d in dirs:
            k = os.path.join(root, d)
            if len(re.findall(r'\\', k))>len(re.findall(r'\\', n)):
                n = k
                
    n = n.replace(path, '')
    depth = len(re.findall(r'\\', n))
    return depth

def rez():
    print('Max глубина папки = ' + str(depth(path)))

path = input('Введите путь к папке: ')
depth(path)
rez()

