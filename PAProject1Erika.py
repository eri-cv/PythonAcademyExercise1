'''
author = 'Erika'
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]
registered = {'bob':'123', 'ann':'pass123', 'mike':'password123', 'liz':'pass123'}
print('-' * 30)
print('Hello, welcome to the app. Please enter your username and password:')
username = input('USERNAME:')
password = input('PASSWORD:')
print('-' * 30)
if registered.get(username) != password:
    print('Your username or password is incorrect.')
else:
    print('We have 3 texts to be analyzed.')
    text_num = int(input('Enter a number btw. 1 and 3:'))

    print('-' * 30)

    words = TEXTS[text_num-1].split()
    w_capital = list()
    w_upper = list()
    w_lower = list()
    w_num = list()
    for word in words:
        word.strip(',.')
        if word.istitle():
            w_capital.append(word)
        elif word.isupper():
            w_upper.append(word)
        elif word.islower():
            w_lower.append(word)
        elif word.isnumeric():
            w_num.append(int(word))

    print('There is', (len(words)), 'words in the selected text.')
    print('There is', (len(w_capital)), 'titlecase words.')
    print('There is', (len(w_upper)), 'uppercase words.')
    print('There is', (len(w_lower)), 'lowercase words.')
    print('There is', (len(w_num)), 'numeric strings.')

    print('-' * 30)
    freq1 = 0
    freq2 = 0
    freq3 = 0
    freq4 = 0
    freq5 = 0
    freq6 = 0
    freq7 = 0
    freq8 = 0
    freq9 = 0
    freq10 = 0

    n = 0
    for word in words:
        if len(word) == 1:
            freq1 += 1
        elif len(word) == 2:
            freq2 += 1
        elif len(word) == 3:
            freq3 += 1
        elif len(word) == 4:
            freq4 += 1
        elif len(word) == 5:
            freq5 += 1
        elif len(word) == 6:
            freq6 += 1
        elif len(word) == 7:
            freq7 += 1
        elif len(word) == 8:
            freq8 += 1
        elif len(word) == 9:
            freq9 += 1
        elif len(word) == 10:
            freq10 += 1

    print('1', '*' * freq1, freq1)
    print('2', '*' * freq2, freq2)
    print('3', '*' * freq3, freq3)
    print('4', '*' * freq4, freq4)
    print('5', '*' * freq5, freq5)
    print('6', '*' * freq6, freq6)
    print('7', '*' * freq7, freq7)
    print('8', '*' * freq8, freq8)
    print('9', '*' * freq9, freq9)
    print('10', '*' * freq10, freq10)

    print('-' * 30)

    num_total = sum(w_num)
    print('If we summed all the numbers in this text we eould get:', num_total)

    print('-' * 30)







