from tools import get_input, first_half_of, last_half_of, get_seat_id


def get_passes_sorted() -> list:
    '''
    Similar to Part 1 of Day 5, we gather all the IDs
    in a list instead of just keeping track of the max.
    Then, we'll sort the list.
    '''
    boarding_passes = get_input()

    board_pass_ids = []
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

        board_pass_ids.append(get_seat_id(rows[0], columns[0]))

    board_pass_ids.sort()

    return board_pass_ids


def get_my_seat() -> int:
    '''
    We were told that our seat is the only empty one,
    and we're somewhere in the middle, and that IDs +1
    and -1 (each side of us) is taken. Just iterate
    through the sorted IDs until we find one where the
    +1 is missing, that is our seat.
    '''
    board_pass_ids = get_passes_sorted()

    for pi in board_pass_ids:
        if pi + 1 not in board_pass_ids:
            return pi + 1

    return board_pass_ids


print(get_my_seat())
