from tools import get_input


def day_15():
    values = [9, 3, 1, 0, 8, 4]

    for itr in range(7, 30000001):
        curr = values[-1]
        # print('Checking on curr: ', curr)
        found = False
        for i in range(len(values) - 2, -1, -1):
            # print(values[i], ' -> ', curr)
            if values[i] == curr:
                # print('Found, appending ', i)
                values.append(itr - i - 2)
                found = True
                break
        if not found:
            values.append(0)
    return values.pop()


results = day_15()

print('Puzzle Answer: ', results)

assert results == 436
