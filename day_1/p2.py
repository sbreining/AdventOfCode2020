import os


def get_input():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(dir_path, "input.txt"), "r") as infile:
        report = infile.readlines()
    return report


def get_product(report):
    for i in range(len(report) - 2):
        for j in range(len(report) - 1):
            for k in range(len(report)):
                sum_ = int(report[i]) + int(report[j]) + int(report[k])
                if sum_ == 2020:
                    return int(report[i]) * int(report[j]) * int(report[k])


expense_report = get_input()

product = get_product(expense_report)

print(product)
