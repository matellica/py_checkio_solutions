#!/usr/bin/env checkio --domain=py run sort-array-by-element-frequency
# https://py.checkio.org/mission/sort-array-by-element-frequency/


def frequency_sort(items):
    from collections import Counter
    counter = Counter(items)
    res_list = []
    for key, val in counter.most_common():
        for x in range(val):
            res_list.append(key)
    return res_list


def test_frequency_sort():
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")


if __name__ == '__main__':
    test_frequency_sort()
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))
