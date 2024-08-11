x, y = [int(i) for i in input().split()]

while x != 0 and y != 0:

    if y > 0 and x > 0:
        print('primeiro')
    elif y > 0 and x < 0:
        print('segundo')
    elif y < 0 and x < 0:
        print('terceiro')
    else:
        print('quarto')

    x, y = [int(i) for i in input().split()]

