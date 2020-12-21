from tools import get_input


def all_possible(key, rules):
    '''
    Just going to test adding this comment
    so I can make sure that I got my key
    set up correct in github.
    '''
    strings = []

    if rules[key] == 'a' or rules[key] == 'b':
        return rules[key]

    for keys in rules[key]:
        values = keys.split(' ')
        string = ''
        for val in values:
            result = all_possible(val, rules)
            if result == 'a' or result == 'b':
                string += result

        strings.append(string)

    return strings


def map_rules(rules):
    parsed_rules = {}
    for rule in rules:
        some = rule.split(':')
        sub_rules = some[1].split('|')
        vals = []
        for sub in sub_rules:
            r = sub.strip()
            if r == '"a"' or r == '"b"':
                vals = sub[2]
            else:
                vals.append(sub.strip())
        parsed_rules[some[0]] = vals

    return parsed_rules


def day_19():
    values = get_input()
    values = values.split('\n\n')

    rules = values[0].split('\n')

    rules = map_rules(rules)

    possibles = all_possible('0', rules)
    print('Possibles:', possibles)
    return rules
    text = values[1].split('\n')

    count = 0
    for possible in rules:
        if possible in text:
            count += 1

    return count


results = day_19()

print('Puzzle Answer:', results)
