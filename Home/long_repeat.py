#!/usr/bin/env checkio --domain=py run long-repeat
# https://py.checkio.org/mission/long-repeat/
# END_DESC
import util


@util.measure
def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    # from collections import Counter
    # return Counter(list(line)).most_common()[0][1]
    same_char = None
    counter = 0
    most_common = 0
    for char in line:
        if same_char is None:
            same_char = char

        if char == same_char:
            counter += 1
        else:
            if most_common < counter:
                most_common = counter
            same_char = char
            counter = 1
    if most_common == 0:
        most_common = counter
    return most_common


@util.measure
def long_repeat2(string):
    from itertools import groupby
    if not string: return 0
    return max(len(list(g)) for _, g in groupby(string))


@util.measure
def long_repeat3(x):
    result = 0
    for y in x+'#':         # iterate over all possible characters (actually '#' is to 
                            # prevent from creating empty sequence for max function
                            # not important in this case)
        for z in range(71): # iterate over all possible sizes, limited to 71 just for fun
            if y*z in x:    # check if group exits, example check if 'a'*3 -> 'aaa' in x
                result = max(result, z) # calculate max group size
    return result


@util.measure
def long_repeat4(x):
    long_repeat4_lambda(x)

long_repeat4_lambda=lambda x:max(z for y in x+'#'for z in range(71)if y*z in x)


@util.measure
def long_repeat5(line):
    data = "".join(['1' if line[i] == line[i + 1] else '0' for i in range(len(line) - 1)])
    return (len(max(data.split('0'))) + 1 if data else 0)


@util.measure
def long_repeat5(x):
    long_repeat5_lambda(x)

long_repeat5_lambda=lambda l:len(l)and max(map(len,dict(__import__('re').findall(r'((.)\2*)',l))))

def test_checkio():
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('aa') == 2, "Fourth"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')


def measure_func(func, evals):
    for ev in evals:
        eval(f'{func}({"ev"})')
        for idx in range(2,10):
            funcname = f'{func}{idx}'
            if funcname in globals():
                eval(f'{func}{idx}({"ev"})')
            else:
                break
        util.print_scores()


if __name__ == '__main__':
    # test_checkio()
    evals = [
        'ddvvrwwwrggg',
        util.random_string(10240)
    ]
    measure_func('long_repeat', evals)
