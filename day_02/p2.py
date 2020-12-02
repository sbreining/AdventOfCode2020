from tools import get_input, parse_string


def num_of_valid_passwords(pass_list):
    '''
    In this version of the password validation, it requires an XOR of sorts.
    Instead of the two numbers in the input representing a range for the
    required character, they represent two positions in the password string.
    Keep in mind those positions are not 0-index based. Instead, the required
    character is expected to be at one of the two positions, but not both. If
    that is true, we'll increment valid_passwords.
    '''
    valid_passwords = 0
    for item in pass_list:
        (pos_1, pos_2, req_char, password) = parse_string(item)

        is_pos_1 = password[int(pos_1) - 1] == req_char

        if password[int(pos_2) - 1] == req_char:
            if not is_pos_1:
                valid_passwords += 1
        else:
            if is_pos_1:
                valid_passwords += 1

    return valid_passwords


print(num_of_valid_passwords(get_input()))
