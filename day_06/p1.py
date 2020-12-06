from string import ascii_lowercase
from tools import get_input


def day_6():
    passports = get_input()

    count = 0
    for passport in passports:
        for c in ascii_lowercase:
            if c in passport:
                count += 1

    return count


print(day_6())
