from tools import get_input
import re


def get_passports():
    input_ = get_input()
    passports = []

    tempstring = ""
    for passport in input_:
        if passport != '':
            tempstring += passport
        else:
            passports.append(tempstring)
            tempstring = ""

    # Add remaining passport if any.
    if tempstring:
        passports.append(tempstring)

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


def is_valid_hcl(hcl: str) -> bool:
    hcl = hcl[1:]

    if len(hcl) != 6:
        return False

    return re.match(r'^[a-z0-9]{6}$', hcl) != None


def is_valid_ecl(ecl: str) -> bool:
    return ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def is_valid_pid(pid: str) -> bool:
    if len(pid) != 9:
        return False

    try:
        int(pid)
    except:
        return False

    return True


def day_4():
    passports = get_passports()

    good_passports = 0
    for passport in passports:
        required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
        is_valid = True
        while required_fields:
            field = required_fields.pop()

            if field == 'byr':
                prog = re.compile('.*byr:(.{4})')
                byr = prog.match(passport)
                if byr == None:
                    is_valid = False
                    break
                byr = byr.group(1)
                if not is_valid_byr(byr):
                    is_valid = False
            elif field == 'iyr':
                prog = re.compile('.*iyr:(.{4})')
                iyr = prog.match(passport)
                if iyr == None:
                    is_valid = False
                    break
                iyr = iyr.group(1)
                if not is_valid_iyr(iyr):
                    is_valid = False
                    break
            elif field == 'eyr':
                prog = re.compile('.*eyr:(.{4})')
                eyr = prog.match(passport)
                if eyr == None:
                    is_valid = False
                    break
                eyr = eyr.group(1)
                if not is_valid_eyr(eyr):
                    is_valid = False
                    break
            elif field == 'hgt':
                prog = re.compile('.*hgt:(\d{2,3}(in|cm))')
                hgt = prog.match(passport)
                if hgt == None:
                    is_valid = False
                    break
                hgt = hgt.group(1)
                if not is_valid_hgt(hgt):
                    is_valid = False
                    break
            elif field == 'hcl':
                prog = re.compile('.*hcl:(#.{6})')
                hcl = prog.match(passport)
                if hcl == None:
                    is_valid = False
                    break
                hcl = hcl.group(1)
                if not is_valid_hcl(hcl):
                    is_valid = False
                    break
            elif field == 'ecl':
                eclprog = re.compile('.*ecl:(.{3})')
                ecl = eclprog.match(passport)
                if ecl == None:
                    is_valid = False
                    break
                ecl = ecl.group(1)
                if not is_valid_ecl(ecl):
                    is_valid = False
                    break
            elif field == 'pid':
                pid = re.match(r'.*pid:(\d{9})', passport)
                if pid == None:
                    is_valid = False
                    break
                pid = pid.group(1)
                if not is_valid_pid(pid):
                    is_valid = False
                    break
        if is_valid:
            good_passports += 1

    return good_passports


print(day_4())
