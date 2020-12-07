from tools import get_input


def get_colors(bags):
    if bags == 'no other bags.':
        return []

    colors = bags.split(', ')
    final_colors = []
    for color in colors:
        temp = color.split(' ')

        final_colors.append(temp[0]+' '+temp[1]+' '+temp[2])

    return final_colors


def count_bags(bag, graph):
    num_col = bag.split(' ')
    count = int(num_col[0])

    count = count  # TODO Pick it up here.

    return count


def day_07():
    rules = get_input()

    graph = {}
    for rule in rules:
        bags = rule.split(' bags contain ')
        if graph.get(bags[0]) is not None:
            graph[bags[0]] += get_colors(bags[1])
        else:
            graph[bags[0]] = get_colors(bags[1])
        graph[bags[0]] = list(dict.fromkeys(graph[bags[0]]))

    print(graph)
    count = 0

    for bag in graph['shiny gold']:
        count += count_bags(bag, graph)

    return count


print(day_07())
