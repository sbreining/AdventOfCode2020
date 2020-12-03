from tools import get_input


def count_trees(tree_map):
    trees = 0
    x = y = 0
    while x < len(tree_map):
        if tree_map[x][y] == '#':
            trees += 1
        y = (y + 3) % (len(tree_map[0]) - 1)
        x += 1

    return trees


print(count_trees(get_input()))
