import math
print('it is a calk')
while True:
    print('\n write nums')
    while True:
        try:
            x = float(input())
            break
        except ValueError:
            print('Erorr. write nums ')
    while True:
        try:
            y = float(input())
            break
        except ValueError:
            print('Erorr. write nums ')
    print('numbers and mean')
    print('1 = **', '2 = *', '3 = /', '4 = +', '5 = -')
    while True:
        try:
            mean_1 = int(input())
            if 1 <= mean_1 <= 5: 
                break
            else:
                print('No comands. Write nums')
        except ValueError:
            print('No comands, write nums.')
    if mean_1 == 1:
        print('Results', pow (x, y))
    elif mean_1 == 2:
        print('Results', x*y)
    elif mean_1 == 3:
        if y == 0:
            print('Error, zero del')
        else:
            print('Results', x/y)
    elif mean_1 == 4:
        print('Results', x+y)
    elif mean_1 == 5:
        print('Results', x-y)
    print('\nactions exit or stay')
    ans = input()
    if ans == 'exit':
        print('program completion')
        break
    elif ans == 'stay':
        print('Next')