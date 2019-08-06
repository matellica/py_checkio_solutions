#!/usr/bin/env checkio --domain=py run sort-array-by-element-frequency
# https://py.checkio.org/mission/sort-array-by-element-frequency/


def frequency_sort(items):
    from collections import Counter
    counter = Counter(items)
    res_list = []
    for key, val in counter.items():
        for x in range(val):
            res_list.append(key)
    return res_list


def frequency_sort2(items):
    # vlad.bezden
    from collections import Counter
    c = Counter(items)
    result = sorted(c.elements(), key=lambda k: c[k], reverse=True)
    return result


def test_frequency_sort():
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")


if __name__ == '__main__':
    test_frequency_sort()
    # print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))


    from timeit import timeit
    items = [4,6,2,4,5,6,7,2,3,4,6,5,3,1,4,4,5,6]
    for f in [frequency_sort, frequency_sort2]:
        t = timeit(stmt="f(items)", number=100, globals=globals())
        print(f"{f.__name__} took: {t:.6f}")
