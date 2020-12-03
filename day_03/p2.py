from tools import get_input


def day_3(down, right, tree_map):
    trees = 0
    x = y = 0
    while x < len(tree_map):
        if tree_map[x][y] == '#':
            trees += 1
        y = (y + right) % (len(tree_map[0]) - 1)
        x += down

    return trees


d1_r1 = day_3(1, 1, get_input())

d1_r3 = day_3(1, 3, get_input())

d1_r5 = day_3(1, 5, get_input())

d1_r7 = day_3(1, 7, get_input())

d2_r1 = day_3(2, 1, get_input())

print(d1_r1 * d1_r3 * d1_r5 * d1_r7 * d2_r1)
