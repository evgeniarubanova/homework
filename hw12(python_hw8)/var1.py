def dict(file):
    with open(file, "r", encoding = 'utf-8') as j:
        st = j.readlines()
        for i in range(len(st)):
            st[i] = st[i].strip("\n")
    ex = {}
    for i in range(len(st)):
        words = st[i].split(' ')
        ex[words[0]] = words[1]
    return ex

def guess():
    ex = dict("file.csv")
    for key in ex:
        print(ex[key], '...')
        p = input('Попробуйте угадать существительное: ')
        i = 1
        while i != len(key):
            
            if p == key:
                print("Поздравляем! Вы угадали.")
                break
            else:
                p = input("Увы, Вы не угадали. Попробуйте еще раз: ")
                i += 1

        
guess()
  
    
