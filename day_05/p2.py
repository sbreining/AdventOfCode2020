from tools import get_input


def get_seat_id(row: int, column: int) -> int:
    '''
    The formula for calculating the seat ID.
    '''
    return row * 8 + column


def get_passes_sorted() -> list:
    '''
    Similar to Part 1 of Day 5, we gather all the IDs
    in a list instead of just keeping track of the max.
    Then, we'll sort the list.
    '''
    boarding_passes = get_input()

    pass_ids = []
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

        # We can pop, because there is only 1 element left.
        pass_ids.append(get_seat_id(rows[0], columns[0]))

    pass_ids.sort()

    return pass_ids


def get_my_seat() -> int:
    '''
    We were told that our seat is the only empty one,
    and we're somewhere in the middle, and that IDs +1
    and -1 (each side of us) is taken. Just iterate
    through the sorted IDs until we find one where the
    +1 is missing, that is our seat.
    '''
    pass_ids = get_passes_sorted()

    for pi in pass_ids:
        if pi + 1 not in pass_ids:
            return pi + 1

    return pass_ids


print(get_my_seat())
