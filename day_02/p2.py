from get_input import get_input
import re


def parse_string(item):
    return re.match(r'^(\d+)-(\d+) ([a-z]): ([a-z]+)$', item).groups()


def num_of_valid_passwords(pass_list):
    valid_passwords = 0
    for item in pass_list:
        (pos_1, pos_2, req_char, password) = parse_string(item)

        is_pos_1 = False
        if password[int(pos_1) - 1] == req_char:
            is_pos_1 = True

        if password[int(pos_2) - 1] == req_char:
            if not is_pos_1:
                valid_passwords += 1
        else:
            if is_pos_1:
                valid_passwords += 1

    return valid_passwords


print(num_of_valid_passwords(get_input()))
