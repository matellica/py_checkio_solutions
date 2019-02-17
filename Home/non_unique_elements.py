#!/usr/bin/env checkio --domain=py run non-unique-elements
# https://py.checkio.org/mission/non-unique-elements/


def checkio(data: list) -> list:
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


def test_checkio():
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
    print("It is all good. Let's check it now")


if __name__ == "__main__":
    test_checkio()
