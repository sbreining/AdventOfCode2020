from tools import get_input


def add_layers(hyper_cube):
    # TODO: Pick up here. 4 dimensional space is too much for my brain right now.
    for cube in hyper_cube:
        for square in cube:
            for row in square:
                row.insert(0, '.')
                row.append('.')
            additional = ['.' for _ in range(len(square[0]))]
            square.insert(0, additional)
            square.append(additional)
        hyper_cube.insert(0, cube)

    layer = []
    for i in range(len(cube[0])):
        layer.append([])
        for _ in range(len(cube[0][0])):
            layer[i].append('.')
    cube.insert(0, layer)
    cube.append(layer)

    return cube


def count_neighbors(x, y, z, cube):
    count = 0
    try:
        if cube[x-1][y-1][z-1] == '#':
            count += 1
    except:
        pass
    try:
        if cube[x-1][y-1][z] == '#':
            count += 1
    except:
        pass
    try:
        if cube[x-1][y-1][z+1] == '#':
            count += 1
    except:
        pass
    try:
        if cube[x-1][y][z-1] == '#':
            count += 1
    except:
        pass
    try:
        if cube[x-1][y][z] == '#':
            count += 1
    except:
        pass
    try:
        if cube[x-1][y][z+1] == '#':
            count += 1
    except:
        pass
    try:
        if cube[x-1][y+1][z-1] == '#':
            count += 1
    except:
        pass
    try:
        if cube[x-1][y+1][z] == '#':
            count += 1
    except:
        pass
    try:
        if cube[x-1][y+1][z+1] == '#':
            count += 1
    except:
        pass

    # BREAK

    try:
        if cube[x][y-1][z-1] == '#':
            count += 1
    except:
        pass
    try:
        if cube[x][y-1][z] == '#':
            count += 1
    except:
        pass
    try:
        if cube[x][y-1][z+1] == '#':
            count += 1
    except:
        pass
    try:
        if cube[x][y][z-1] == '#':
            count += 1
    except:
        pass
    try:
        if cube[x][y][z] == '#':
            count += 1
    except:
        pass
    try:
        if cube[x][y][z+1] == '#':
            count += 1
    except:
        pass
    try:
        if cube[x][y+1][z-1] == '#':
            count += 1
    except:
        pass
    try:
        if cube[x][y+1][z] == '#':
            count += 1
    except:
        pass
    try:
        if cube[x][y+1][z+1] == '#':
            count += 1
    except:
        pass

    # Break

    try:
        if cube[x+1][y-1][z-1] == '#':
            count += 1
    except:
        pass
    try:
        if cube[x+1][y-1][z] == '#':
            count += 1
    except:
        pass
    try:
        if cube[x+1][y-1][z+1] == '#':
            count += 1
    except:
        pass
    try:
        if cube[x+1][y][z-1] == '#':
            count += 1
    except:
        pass
    try:
        if cube[x+1][y][z] == '#':
            count += 1
    except:
        pass
    try:
        if cube[x+1][y][z+1] == '#':
            count += 1
    except:
        pass
    try:
        if cube[x+1][y+1][z-1] == '#':
            count += 1
    except:
        pass
    try:
        if cube[x+1][y+1][z] == '#':
            count += 1
    except:
        pass
    try:
        if cube[x+1][y+1][z+1] == '#':
            count += 1
    except:
        pass
    return count


def goes_on(x, y, z, cube):
    return count_neighbors(x, y, z, cube) == 3


def stay_on(x, y, z, cube):
    return 1 < count_neighbors(x, y, z, cube) < 4


def flip_cubes(cube):
    next_cube = []
    for x in range(len(cube)):
        next_cube.append([])
        for y in range(len(cube[0])):
            next_cube[x].append([])
            for z in range(len(cube[0][0])):
                next_cube[x][y].append([])
                for w in range(len(cube[0][0][0])):
                    if cube[x][y][z][w] == '.':
                        next_cube[x][y][z].append(
                            '#' if goes_on(x, y, z, cube) else '.')
                    else:
                        next_cube[x][y][z].append(
                            '#' if stay_on(x, y, z, cube) else '.')
    return next_cube


def day_17():
    values = get_input().splitlines()
    hyper_cube = []
    cube = []
    grid = []
    for val in values:
        grid.append([c for c in val])
    cube.append(grid)
    hyper_cube.append(cube)
    for _ in range(6):
        hyper_cube = add_layers(hyper_cube)
        hyper_cube = flip_cubes(hyper_cube)

    count = 0
    for x in hyper_cube:
        for y in x:
            for z in y:
                for w in z:
                    if w == '#':
                        count += 1
    return count


results = day_17()

print('Puzzle Answer:', results)
