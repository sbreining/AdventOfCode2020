from tools import get_input


def walk_nw(i, j, seat_map):
    # Don't start on the current seat
    i -= 1
    j -= 1
    while i > -1 and j > -1:
        if seat_map[i][j] == '#':
            return False
        elif seat_map[i][j] == 'L':
            return True

        i -= 1
        j -= 1

    return True


def walk_ne(i, j, seat_map):
    # Don't start on the current seat
    i -= 1
    j += 1
    while i > -1 and j < len(seat_map[0]):
        if seat_map[i][j] == '#':
            return False
        elif seat_map[i][j] == 'L':
            return True

        i -= 1
        j += 1

    return True


def walk_se(i, j, seat_map):
    # Don't start on the current seat
    i += 1
    j += 1
    while i < len(seat_map) and j < len(seat_map[0]):
        if seat_map[i][j] == '#':
            return False
        elif seat_map[i][j] == 'L':
            return True

        i += 1
        j += 1

    return True


def walk_sw(i, j, seat_map):
    print('enter walk_sw at (%d, %d)', i, j)
    # Don't start on the current seat
    i += 1
    j -= 1
    while i < len(seat_map) and j > -1:
        if seat_map[i][j] == '#':
            print(i, j, 'false')
            return False
        elif seat_map[i][j] == 'L':
            print(i, j, 'true')
            return True

        i += 1
        j -= 1

    print(i, j, 'true out of loop')
    return True


def walk_w(i, j, seat_map):
    # Don't start on the current seat
    j -= 1
    while j > -1:
        if seat_map[i][j] == '#':
            return False
        elif seat_map[i][j] == 'L':
            return True

        j -= 1

    return True


def walk_e(i, j, seat_map):
    # Don't start on the current seat
    j = 1
    while j < len(seat_map[0]):
        if seat_map[i][j] == '#':
            return False
        elif seat_map[i][j] == 'L':
            return True

        j += 1

    return True


def walk_n(i, j, seat_map):
    # Don't start on the current seat
    i -= 1
    while i > -1:
        if seat_map[i][j] == '#':
            return False
        elif seat_map[i][j] == 'L':
            return True

        i -= 1

    return True


def walk_s(i, j, seat_map):
    # Don't start on the current seat
    i += 1
    while i < len(seat_map):
        if seat_map[i][j] == '#':
            return False
        elif seat_map[i][j] == 'L':
            return True

        i += 1

    return True


def can_sit(i, j, seat_map):
    if not walk_n(i, j, seat_map):
        return False
    if not walk_e(i, j, seat_map):
        return False
    if not walk_s(i, j, seat_map):
        return False
    if not walk_w(i, j, seat_map):
        return False
    if not walk_nw(i, j, seat_map):
        return False
    if not walk_ne(i, j, seat_map):
        return False
    if not walk_sw(i, j, seat_map):
        return False
    if not walk_se(i, j, seat_map):
        return False

    return True


def should_empty(i, j, seat_map):
    count = 0
    if not walk_n(i, j, seat_map):
        count += 1
    if not walk_e(i, j, seat_map):
        count += 1
    if not walk_s(i, j, seat_map):
        count += 1
    if not walk_w(i, j, seat_map):
        count += 1
    if not walk_nw(i, j, seat_map):
        count += 1
    if not walk_ne(i, j, seat_map):
        count += 1
    if not walk_sw(i, j, seat_map):
        count += 1
    if not walk_se(i, j, seat_map):
        count += 1

    return count > 4


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

    itr = 1
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

        print('----' + str(itr) + '----')
        print('----START----')
        pretty_print(seat_map)
        print('-------------')
        pretty_print(next_seats)
        print('----FINISH---')
        if next_seats == seat_map:
            break
        else:
            itr += 1
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

assert results == 26
