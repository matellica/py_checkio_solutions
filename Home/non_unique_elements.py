#!/usr/bin/env checkio --domain=py run non-unique-elements
# https://py.checkio.org/mission/non-unique-elements/

import time
import timeit


def measure(func):
    def wrapper(*args, **kargs):
        start_time = time.perf_counter()

        result = func(*args, **kargs)

        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f'{func.__name__}: {execution_time}')
        return result
    return wrapper

@measure
def checkio1(data: list) -> list:
    numbers = {}
    for digit in data:
        numbers[digit] = numbers.get(digit, 0) + 1
    uniq_elements = [key[0] for key in numbers.items() if key[1] == 1]

    non_uniq_elements = []
    for digit in data:
        if digit in uniq_elements:
            continue
        non_uniq_elements.append(digit)

    return non_uniq_elements


@measure
def checkio2(data: list) -> list:
    return [digit for digit in data if data.count(digit) > 1]


@measure
def checkio3(data: list) -> list:
    from collections import Counter
    counter = Counter(data)
    return [item for item in data if counter[item] > 1]


@measure
def checkio4(data: list) -> list:
    counter = set(data)
    return [item for item in counter if  > 1]


def test_checkio():
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
    print("It is all good. Let's check it now")


if __name__ == "__main__":
    # test_checkio()
    # lst = list(range(10**1))+[0]
    lst = list(range(10**4))+[0]
    checkio1(lst)
    checkio2(lst)
    checkio3(lst)
    # print(timeit.timeit('checkio1(lst)',setup='from __main__ import checkio1, lst'))
    # checkio1(lst)
    # print(timeit.timeit('checkio2(lst)','from __main__ import checkio2, lst'))
