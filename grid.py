# Draws a grid as below

# + - - - -  + - - - -  +
# |          |          |
# |          |          |
# |          |          |
# |          |          |
# + - - - -  + - - - -  +
# |          |          |
# |          |          |
# |          |          |
# |          |          |
# + - - - -  + - - - -  +

def crosses():
    print('+ ' + '- ' * 4, end =' ')
    print('+ ' + '- ' * 4 , '+')

def lines():
    print('| ' + ' ' * 8, end=' ')
    print('| ' + ' ' * 8, '|')

def four_lines(func):
    lines()
    lines()
    lines()
    lines()

# drawing the grid

def grid():
    # line with crosses
    crosses()

    # 4 lines of vertical lines
    four_lines(lines)

    # line with crosses
    crosses()

    # 4 lines of vertical lines
    four_lines(lines)

    # line with crosses
    crosses()

print(grid())