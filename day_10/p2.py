from tools import get_input


def day_10():
    shit = get_input()

    shit.sort()

    dict = {}
    for i in range(len(shit)):
        dict[shit[i]] = []
        itr = i + 1
        while itr < i+4:
            try:
                if shit[itr] - shit[i] <= 3:
                    dict[shit[i]].append(shit[itr])
            except:
                pass
            itr += 1

    permutations = 1
    for value in dict.values():
        if not value:
            pass
        else:
            permutations *= len(value)
    return permutations


print(day_10())
