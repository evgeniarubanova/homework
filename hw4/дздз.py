print('Введите слово')
word = input()
for index,letter in enumerate(word): 
    if index%2!=0 and letter!='к'and letter!='а':
        print(letter)

