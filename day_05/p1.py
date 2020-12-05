from tools import get_input


def get_seat_id(row: int, column: int) -> int:
    '''
    The formula for calculating the seat ID.
    '''
    return row * 8 + column


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
                rows = rows[:int(len(rows)/2)]
            elif letter == 'B':
                rows = rows[int(len(rows)/2):]
            elif letter == 'R':
                columns = columns[int(len(columns)/2):]
            elif letter == 'L':
                columns = columns[:int(len(columns)/2)]

        current_max = max(current_max, get_seat_id(rows[0], columns[0]))

    return current_max


print(max_boarding_pass_id())
