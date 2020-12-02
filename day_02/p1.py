from get_input import get_input
import re


def parse_string(item):
    return re.match(r'^(\d+)-(\d+) ([a-z]): ([a-z]+)$', item).groups()


def num_of_valid_passwords(pass_list):
    valid_passwords = 0
    for item in pass_list:
        (min_, max_, req_char, password) = parse_string(item)

        letter_count = 0
        for letter in password:
            if letter == req_char:
                letter_count += 1

        if int(min_) <= letter_count <= int(max_):
            valid_passwords += 1

    return valid_passwords


print(num_of_valid_passwords(get_input()))
