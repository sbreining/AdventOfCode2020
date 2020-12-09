from tools import get_input

invalid = 675280050

def day_9():
    shit = get_input()

    contiguous = 2
    while contiguous < len(shit):
        itr=0
        while itr + contiguous < len(shit):
            cont_nums = shit[itr:itr+contiguous]
            if sum(cont_nums) == invalid:
                cont_nums.sort()
                return cont_nums[0] + cont_nums.pop()
            itr += 1
            if itr + contiguous == len(shit):
                break
        contiguous+=1

print(day_9())
