def fermat(a, b, c, n):
    left = a ** n + b ** n
    right = c ** n

    if left == right:
        print('Holy smokes, Fermat was wrong!')
    else:
        print('No, that doesn\'t work')

fermat(2, 1, 2, 3)