from tools import get_input
import re


def day_4():
    passports = get_input()
    new_list = []

    tempstring = ""
    # TODO: Look at this loop.
    for passport in passports:
        if passport != '':
            tempstring += passport
        else:
            new_list.append(tempstring)
            tempstring = ""

    good_passports = 0

    for item in new_list:
        required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
        col_pos = item.find(':')
        print(item)
        while col_pos > 0:
            pp_data = item[col_pos-3:col_pos]
            try:
                required_fields.remove(pp_data)
            except ValueError:
                pass
            item = item[col_pos+1:]
            col_pos = item.find(':')
        if required_fields == []:
            good_passports += 1

    return good_passports


print(day_4())
