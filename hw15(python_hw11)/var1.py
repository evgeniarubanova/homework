import re

def open_file():
    with open('Комар.html', 'r', encoding = 'utf-8') as j:
        text = j.read()
    return text

r_k = r'(комар)(ы|е|(а(х|(ми?))?)|о[мв]|у)?'
r_K = r'(Комар)(ы|е|(а((ми?)|х)?)|о[мв]|у)?'

def replace():
    text = open_file()
    r = re.search(r_k, text)
    if r:
        text = re.sub(r.group(1), 'слон', text)
    r = re.search(r_K, text)
    if r:
        text = re.sub(r.group(1), 'Слон', text)
    return text

def writedown():
    text = replace()
    with open ('note.html', 'a', encoding = 'utf-8') as j:
        j.write(text)

replace()   
writedown()

