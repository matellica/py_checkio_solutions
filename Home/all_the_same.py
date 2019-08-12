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


@util.measure
def all_the_same2(elements: List[Any]) -> bool:
    all_the_same2_lambda(elements)

all_the_same2_lambda = lambda e: e[1:] == e[:-1]


@util.measure
def all_the_same3(elements: List[Any]) -> bool:
    return len(set(elements)) <= 1


@util.measure
def all_the_same4(elements):
   return elements == elements[1:] + elements[:1]


@util.measure
def all_the_same5(elements):
    el = iter(elements)
    first = next(el, None)
    return all(element == first for element in el)


def test_checkio():
    # These "asserts" are used for self-checking and not for an auto-testing
    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")


if __name__ == '__main__':
    # test_checkio()
    evals = [
        [1, 1, 1],
        [1, 2, 1],
        ['a', 'a', 'a'],
        list(range(10**7)),
    ]
    for ev in evals:
        all_the_same(ev)
        all_the_same2(ev)
        all_the_same3(ev)
        all_the_same4(ev)
        all_the_same5(ev)
        util.print_scores()
