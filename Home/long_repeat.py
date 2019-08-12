#!/usr/bin/env checkio --domain=py run long-repeat
# https://py.checkio.org/mission/long-repeat/
# END_DESC
from collections import Counter

def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
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


def test_checkio():
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('aa') == 2, "Fourth"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')


if __name__ == '__main__':
    test_checkio()
