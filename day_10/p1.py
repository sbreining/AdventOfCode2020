from tools import get_input


def day_10():
    shit = get_input()

    dict = {
        1: 0,
        2: 0,
        3: 0
    }
    shit.sort()
    dict[shit[0]] += 1
    for itr in range(len(shit) - 1):
        dict[shit[itr+1] - shit[itr]] += 1
    dict[3] += 1
    return dict[1] * dict[3]


print(day_10())
