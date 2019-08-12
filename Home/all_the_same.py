#!/usr/bin/env checkio --domain=py run all-the-same
# https://py.checkio.org/mission/all-the-same/
# END_DESC

from typing import List, Any
import util


@util.measure
def all_the_same(elements: List[Any]) -> bool:
    for element in elements:
        if element != elements[0]:
            return False
    return True


def test_checkio():
    # These "asserts" are used for self-checking and not for an auto-testing
    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")


if __name__ == '__main__':
    test_checkio()
    evals = [
        [1, 1, 1],
        [1, 2, 1],
        ['a', 'a', 'a'],
    ]
    for ev in evals:
        all_the_same(ev)
        util.print_scores()
