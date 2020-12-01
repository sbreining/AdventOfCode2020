import os


def get_input():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(dir_path, "input.txt"), "r") as infile:
        report = infile.readlines()
    return report


def get_product(report):
    i = 0
    while i < len(report) - 2:
        j = 1 + i
        while j < len(report) - 1:
            first = int(report[i])
            second = int(report[j])
            if first + second >= 2020:
                j += 1
                continue
            k = 1 + j
            while k < len(report):
                third = int(report[k])
                sum_ = first + second + third
                if sum_ == 2020:
                    return first * second * third
                k += 1
            j += 1
        i += 1


expense_report = get_input()

product = get_product(expense_report)

print(product)
