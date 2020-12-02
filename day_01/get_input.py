from os.path import dirname, realpath, join


def get_input():
    dir_path = dirname(realpath(__file__))
    with open(join(dir_path, "input.txt"), "r") as infile:
        report = infile.readlines()
    return report
