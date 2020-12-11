from tools import get_input


def can_sit(i, j, seat_map):
    try:
        if i < 1 or j < 1:
            pass
        elif seat_map[i-1][j-1] == '#':
            return False
    except:
        pass

    try:
        if i < 1:
            pass
        elif seat_map[i-1][j] == '#':
            return False
    except:
        pass

    try:
        if i < 1:
            pass
        elif seat_map[i-1][j+1] == '#':
            return False
    except:
        pass

    try:
        if j < 1:
            pass
        elif seat_map[i][j-1] == '#':
            return False
    except:
        pass

    try:
        if seat_map[i][j+1] == '#':
            return False
    except:
        pass

    try:
        if j < 1:
            pass
        elif seat_map[i+1][j-1] == '#':
            return False
    except:
        pass

    try:
        if seat_map[i+1][j] == '#':
            return False
    except:
        pass

    try:
        if seat_map[i+1][j+1] == '#':
            return False
    except:
        pass

    return True


def should_empty(i, j, seat_map):
    count = 0
    try:
        if i < 1 or j < 1:
            pass
        elif seat_map[i-1][j-1] == '#':
            count += 1
    except:
        pass

    try:
        if i < 1:
            pass
        elif seat_map[i-1][j] == '#':
            count += 1
    except:
        pass

    try:
        if i < 1:
            pass
        elif seat_map[i-1][j+1] == '#':
            count += 1
    except:
        pass

    try:
        if j < 1:
            pass
        elif seat_map[i][j-1] == '#':
            count += 1
    except:
        pass

    try:
        if seat_map[i][j+1] == '#':
            count += 1
    except:
        pass

    try:
        if j < 1:
            pass
        elif seat_map[i+1][j-1] == '#':
            count += 1
    except:
        pass

    try:
        if seat_map[i+1][j] == '#':
            count += 1
    except:
        pass

    try:
        if seat_map[i+1][j+1] == '#':
            count += 1
    except:
        pass

    return count > 3


def pretty_print(matrix):
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = ' '.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print('\n'.join(table))


def day_11():
    values = get_input()

    seat_map = []
    for val in values:
        seat_map.append(list(val))

    while True:
        next_seats = []
        for i in range(len(seat_map)):
            next_seats.append([])
            for j in range(len(seat_map[0])):
                if seat_map[i][j] == '.':
                    next_seats[i].append('.')
                elif seat_map[i][j] == 'L':
                    if can_sit(i, j, seat_map):
                        next_seats[i].append('#')
                    else:
                        next_seats[i].append('L')
                else:
                    if should_empty(i, j, seat_map):
                        next_seats[i].append('L')
                    else:
                        next_seats[i].append('#')

        if next_seats == seat_map:
            break
        else:
            seat_map = next_seats
            next_seats = []

    count = 0
    for row in seat_map:
        for chair in row:
            if chair == '#':
                count += 1

    return count


results = day_11()

print(results)
