import os


def get_input():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(dir_path, "input.txt"), "r") as infile:
        report = infile.readlines()
    return report


def get_product(report):
    dictionary = {}

    for i in range(len(report)):
        num = int(report[i])
        compliment = 2020 - num

        if dictionary.get(compliment) is not None:
            return compliment * num

        dictionary[num] = i


expense_report = get_input()

product = get_product(expense_report)

print(product)
