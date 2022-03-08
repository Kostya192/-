# https://pythonworld.ru/tipy-dannyx-v-python/stroki-funkcii-i-metody-strok.html
# https://pythonworld.ru/tipy-dannyx-v-python/spiski-list-funkcii-i-metody-spiskov.html
# https://pythonworld.ru/moduli/modul-random.html

import random # библиотека random для случайного слова из списка a

print('Вы попали в поле чудес!!')
print('Напиши !start и мы начнём игру!')

game = input()
if game == '!start':
    print('Погнали')
    
    a = ['кресло','дед','душ','диван','кровать'] # список слов
    
    s = random.choice(a) # рандомное слово
    s1 = s # такое же рандомное слово
    
    for elem in s:
        s = s.replace(elem, '*')
    
    l = s.count('*')
    print(s)
    
    k = 0
    ind = 0 # индекс в котором находится буква
    ch = input() # вводим букву
    word = ch.split()
    rounds = 1 # количество попыток
    stop = 10
    while stop > 0:       
        if word == s1.split():
            print('УРА!')
            print(s1)
            break   
        if len(word) > 1:
            print('ERROR')        
        if (len(word) == 1 or (ord(a) >= 65 and ord(a) <= 90) or (ord(a) >= 97 and ord(a) <= 122)):
            if ch in s1:
                for el in s1:
                    if el == ch:
                        ind = s1.find(ch)
                print('Not bad')
                s = s[:ind] + ch + s[ind+1:]
                l -= 1
                if s == s1:
                    print('УРА!')
                    print(s1)
                    break
            else:
                print('ERROR')
            print(s)
            rounds += 1
        else:
            print('ERROR')
            rounds += 1
        ch = input()
        stop -= 1
    if stop == 0 or s != s1:
        print("В следующий раз повезёт. Не расстраивайся")
    elif stop != 0:
        print("Вы совершили -", rounds, "попыток")