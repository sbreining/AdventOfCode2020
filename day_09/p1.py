from tools import get_input

preamble = 25

def day_9():
    shit = get_input()
    itr = preamble
    while itr < len(shit):
        i = itr - preamble
        val_to_check = shit[itr]
        has_pair = False
        while i < itr:
            comp = val_to_check - shit[i]
            if comp in shit[i:itr]:
                has_pair = True
                break
            i+=1
        if not has_pair:
            return val_to_check
        itr += 1
    return -1

print(day_9())
