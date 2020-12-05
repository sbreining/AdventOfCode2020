from os.path import dirname, realpath, join
import re


def get_input() -> list:
    dir_path = dirname(realpath(__file__))
    with open(join(dir_path, "input.txt"), "r") as infile:
        report = infile.readlines()
    return report


def get_passports():
    input_ = get_input()
    passports = []

    tempstring = ""
    for line in input_:
        if line != '\n':
            tempstring += (" " + line.strip())
        else:
            passports.append(tempstring.strip())
            tempstring = ""

    # Add remaining passport if any.
    if tempstring:
        passports.append(tempstring.strip())

    return passports


def is_valid_byr(byr: str) -> bool:
    try:
        byr = int(byr)
    except:
        return False

    return 1920 <= byr <= 2002


def is_valid_iyr(iyr: str) -> bool:
    try:
        iyr = int(iyr)
    except:
        return False

    return 2010 <= iyr <= 2020


def is_valid_eyr(eyr: str) -> bool:
    try:
        eyr = int(eyr)
    except:
        return False

    return 2020 <= eyr <= 2030


def is_valid_hgt(hgt: str) -> bool:
    pos = hgt.find('cm')
    is_cm = True
    if pos < 0:
        is_cm = False
        pos = hgt.find('in')

    if pos < 0:
        return False

    str_val = hgt[:pos]
    val = 0
    try:
        val = int(str_val)
    except:
        return False

    if is_cm:
        return 150 <= val <= 193
    else:
        return 59 <= val <= 76


def day_4():
    passports = get_passports()

    good_passports = 0
    for passport in passports:
        required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
        is_valid = True
        while required_fields:
            field = required_fields.pop()
            if field == 'byr':
                byr = re.match(r'.*byr:(\d{4})', passport)
                if byr == None:
                    is_valid = False
                    break
                byr = byr.group(1)
                if not is_valid_byr(byr):
                    is_valid = False
            elif field == 'iyr':
                iyr = re.match(r'.*iyr:(\d{4})', passport)
                if iyr == None:
                    is_valid = False
                    break
                iyr = iyr.group(1)
                if not is_valid_iyr(iyr):
                    is_valid = False
                    break
            elif field == 'eyr':
                eyr = re.match(r'.*eyr:(\d{4})', passport)
                if eyr == None:
                    is_valid = False
                    break
                eyr = eyr.group(1)
                if not is_valid_eyr(eyr):
                    is_valid = False
                    break
            elif field == 'hgt':
                hgt = re.match(r'.*hgt:(\d{2,3}(in|cm))', passport)
                if hgt == None:
                    is_valid = False
                    break
                hgt = hgt.group(1)
                if not is_valid_hgt(hgt):
                    is_valid = False
                    break
            elif field == 'hcl':
                hcl = re.match(r'.*hcl:#[a-f0-9]{6}', passport)
                if hcl == None:
                    is_valid = False
                    break
            elif field == 'ecl':
                ecl = re.match(
                    r'.*ecl:(amb|blu|brn|gry|grn|hzl|oth)', passport)
                if ecl == None:
                    is_valid = False
                    break
            elif field == 'pid':
                pid = re.match(r'.*pid:(\d{9})', passport)
                if pid == None:
                    is_valid = False
                    break

        if is_valid:
            good_passports += 1

    return good_passports


print(day_4())
