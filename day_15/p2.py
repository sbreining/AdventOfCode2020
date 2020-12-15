from tools import get_input


def day_15():
    dictionary = {9: [1], 3: [2], 1: [3], 0: [4], 8: [5], 4: [6]}
    # dictionary = {0: [1], 3: [2], 6: [3]} # Answer: 436
    # dictionary = {1: [1], 3: [2], 2: [3]} # Answer: 1
    # dictionary = {2: [1], 1: [2], 3: [3]} # Answer: 10
    # dictionary = {3: [1], 1: [2], 2: [3]}  # Answer: 1836

    curr = 4
    for itr in range(7, 30000001):
        if dictionary.get(curr) is not None:
            if len(dictionary.get(curr)) > 1:
                positions = dictionary.get(curr).copy()
                curr = positions.pop() - positions.pop()
                if dictionary.get(curr) is not None:
                    dictionary[curr].append(itr)
                else:
                    dictionary[curr] = [itr]
            else:
                if dictionary.get(0) is not None:
                    dictionary[0].append(itr)
                else:
                    dictionary[0] = [itr]
                curr = 0

    return curr


results = day_15()

print('Puzzle Answer: ', results)
