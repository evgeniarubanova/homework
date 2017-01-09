import random

def adjectives():
    with open('adjectives.txt','r', encoding = 'utf-8') as j:
        adjectives = j.read().split('\n')      
    return random.choice(adjectives)

def noun_f():
    with open('noun_f.txt','r', encoding = 'utf-8') as j:
        noun_f = j.read().split('\n')      
    return random.choice(noun_f)

def marks():
    with open('marks.txt','r', encoding = 'utf-8') as j:
        marks = j.read().split('\n')      
    return random.choice(marks)

def verb_imp():
    with open('verb_imp.txt','r', encoding = 'utf-8') as j:
        verb_imp = j.read().split('\n')      
    return random.choice(verb_imp)

def poss():
    with open('poss.txt','r', encoding = 'utf-8') as j:
        poss = j.read().split('\n')      
    return random.choice(poss)

def noun_obl():
    with open('noun_obl.txt','r', encoding = 'utf-8') as j:
        noun_obl = j.read().split('\n')      
    return random.choice(noun_obl)

def prep_conj():
    with open('prep_conj.txt','r', encoding = 'utf-8') as j:
        prep_conj = j.read().split('\n')      
    return random.choice(prep_conj)

def verb_imp_2():
    with open('verb_imp_2.txt','r', encoding = 'utf-8') as j:
        verb_imp_2 = j.read().split('\n')      
    return random.choice(verb_imp_2)

def adv():
    with open('adv.txt','r', encoding = 'utf-8') as j:
        adv = j.read().split('\n')      
    return random.choice(adv)

def line1():
    return adjectives() + ' ' + noun_f() + marks()

def line2():
    return verb_imp() + ' ' + poss() + ' ' + noun_obl() + marks()

def line3():
    return prep_conj() + ' ' + verb_imp_2() + ' ' + adv() + marks()



print(line1())
print(line2())
print(line3())
