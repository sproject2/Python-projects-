import random
while True:  
    print ('Guess whether a number is even or odd.')
    x = input('Enter your answer: even/odd ')
    if x not in ['even', 'odd']:
        print ('Enter Error')
        continue
    else:
        y = random.randint(0, 10000)
        print (y)
        if y % 2 == 0:
            y = 'even'
        else:
            y = 'odd'
        if y == x:
            print ('win')    
        else:
            print ('Lose')
    while True:
        ag = input('stay or exit: ')
        if ag not in ['stay', 'exit']:
            print ('error')
            continue
        else:
            break
    if ag == 'stay':
        continue
    if ag == 'exit':
        break