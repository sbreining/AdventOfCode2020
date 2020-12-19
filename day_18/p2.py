from tools import get_input


def resolve_parens(eqtn):
    opening = eqtn.find('(')

    if opening == -1:
        closing = eqtn.find(')')

        if closing == -1:
            print('Calculating Equation:', eqtn)
            return str(calculate(eqtn))

        new_eq = str(calculate(eqtn[:closing])) + eqtn[closing+1:]
        print('New equation:', new_eq)
        return new_eq

    return resolve_parens(eqtn[0:opening] + resolve_parens(eqtn[opening+1:]))


def calculate(eqtn):
    print('Inside calculate():', eqtn)
    pieces = eqtn.split(' ')

    print('Here are the pieces:', pieces)
    
    if '+' in pieces:
        resolved_sums = []
        itr = 0
        while itr < len(pieces) - 1:
            if pieces[itr] == '+':
                resolved_sums.pop()
                resolved_sums.append(int(pieces[itr-1]) + int(pieces[itr+1]))
            else:
                resolved_sums.append(pieces[itr])
            itr += 1
    else:
        resolved_sums = pieces

    print('Here are the resolved sums:', resolved_sums)

    product = 1
    for val in resolved_sums:
        if val != '*':
            product *= int(val)

    print('calculate() returning:', product)
    return product


def day_18():
    equation = '1 + (2 * 3) + (4 * (5 + 6))'
    equation = resolve_parens(equation)
    return calculate(equation)

    sum_ = 0
    for equation in equations:
        equation = resolve_parens(equation)
        sum_ += int(calculate(equation))

    return sum_

results = day_18()

print('Puzzle Answer:', results)

assert results == 51

