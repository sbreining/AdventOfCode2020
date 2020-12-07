from tools import get_input


def get_colors(bags):
    if bags == 'no other bags.':
        return []

    colors = bags.split(', ')
    final_colors = []
    for color in colors:
        temp = color.split(' ')

        final_colors.append(temp[1]+' '+temp[2])

    return final_colors


def contains_gold(key, value, graph):
    if 'shiny gold' in value:
        return True
    elif not value:
        return False

    for val in value:
        if contains_gold(val, graph[val], graph):
            return True
    return False


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

    count = 0
    for key, value in graph.items():
        if contains_gold(key, value, graph):
            count += 1

    return count


print(day_07())
