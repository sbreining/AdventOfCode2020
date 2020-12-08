from tools import get_input


def day_8(stuff):
    acc = 0
    itr = 0
    while itr < len(stuff):
        temp = stuff[itr].split(' ')

        if len(temp) == 3:
            return -1

        stuff[itr] += ' true'

        if temp[0] == 'acc':
            acc += int(temp[1])
            itr+=1
        elif temp[0] == 'jmp':
            itr += int(temp[1])
        else:
            itr += 1

    return acc

def something():
    stuff = get_input()
    
    acc = 0
    for shit in range(len(stuff)):
        copy = stuff.copy()
        temp = copy[shit].split(' ')
        if temp[0] == 'nop':
            temp[0] = 'jmp'
            copy[shit] = ' '.join(temp)
        elif temp[0] == 'jmp':
            temp[0] = 'nop'
            copy[shit] = ' '.join(temp)
        else:
            continue

        acc = day_8(copy)
        if acc > 0:
            break
            
    return acc


print(something())
