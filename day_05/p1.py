from tools import get_input, first_half_of, last_half_of, get_seat_id


def max_boarding_pass_id() -> int:
    '''
    First, we find the seat, then calculate the ID
    of the seat. Then we just keep track of the max
    ID found, and finally return it at the end.
    '''
    boarding_passes = get_input()

    current_max = -1
    for bp in boarding_passes:
        rows = [i for i in range(128)]
        columns = [i for i in range(8)]

        for letter in bp:
            if letter == 'F':
                rows = first_half_of(rows)
            elif letter == 'B':
                rows = last_half_of(rows)
            elif letter == 'L':
                columns = first_half_of(columns)
            else:
                columns = last_half_of(columns)

        current_max = max(current_max, get_seat_id(rows[0], columns[0]))

    return current_max


print(max_boarding_pass_id())
