def game_state(string):
    rows = [string[:3], string[3:6], string[6:9]]
    columns = [string[:7:3], string[1:9:3], string[2::3]]
    diagonals = [string[::4], string[2:7:2]]

    matrix = rows + columns + diagonals

    if ' ' not in string and 'XXX' not in matrix and 'OOO' not in matrix:
        return 'Draw'
    elif 'XXX' in matrix:
        return 'X wins'
    elif 'OOO' in matrix:
        return 'O wins'


def user_move(coord):
    global cells

    rows = [[one for one in cells[:3]],
            [two for two in cells[3:6]],
            [three for three in cells[6:]]]

    try:
        int(coord[0])
        int(coord[1])
    except ValueError:
        print('You should enter numbers!')
    else:
        if (int(coord[0]) < 1 or int(coord[0]) > 3) \
                or (int(coord[1]) < 1 or int(coord[1]) > 3):
            print('Coordinates should be from 1 to 3!')
        elif rows[int(coord[0]) - 1][int(coord[1]) - 1] != ' ':
            print('This cell is occupied! Choose another one!')
        else:
            rows[int(coord[0]) - 1][int(coord[1]) - 1] = side

            cells = ''.join([j for i in rows for j in i])
            grid(cells)
            return 'Success'


def grid(string):
    print('---------')
    print('|', string[0], string[1], string[2], '|')
    print('|', string[3], string[4], string[5], '|')
    print('|', string[6], string[7], string[8], '|')
    print('---------')


cells = '         '
grid(cells)

side = 'X'
while True:
    coordinates = input('Enter the coordinates: ').split()

    if user_move(coordinates) == 'Success':
        if game_state(cells):
            print(game_state(cells))
            break

    if side == 'X':
        side = 'O'
    else:
        side = 'X'
