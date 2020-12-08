from tools import get_input


def day_8():
    stuff = get_input()

    acc = 0
    itr = 0
    while itr < len(stuff):
        temp = stuff[itr].split(' ')

        if len(temp) == 3:
            break

        stuff[itr] += ' true'

        if temp[0] == 'acc':
            acc += int(temp[1])
            itr+=1
        elif temp[0] == 'jmp':
            itr += int(temp[1])
        else:
            itr += 1

    return acc


print(day_8())
