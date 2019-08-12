#!/usr/bin/env checkio --domain=py run flatten-list
# https://py.checkio.org/mission/flatten-list/
# END_DESC
import time
from decimal import Decimal


def measure(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        execution_time = "{0:.10f}".format(Decimal(execution_time))
        print(f'{func.__name__}: {execution_time}')
        return result
    return wrapper


@measure
def flat_list(array: list) -> list:
    results = []
    flat_list_logic(results, array)
    return results


def flat_list_logic(res: list, array):
    if type(array) is list:
        for data in array:
            flat_list_logic(res, data)
    else:
        res.append(array)


@measure
def flat_list2(array):
    return flat_list_lambda2(array)


flat_list_lambda2=f=lambda d:[d]if int==type(d)else sum(map(f,d),[])


@measure
def flat_list3(l):
    r = []
    def f(l):
        for i in l:
            r.append(i) if type(i) is int else f(i)
    f(l)
    return r


def test_checkio():
    assert flat_list([1, 2, 3]) == [1, 2, 3], "First"
    assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "Second"
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "Third"
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "Four"
    print('Done! Check it')


if __name__ == '__main__':
    # test_checkio()
    evals = [
        [1, [2, 2, 2], 4],
        [[[2]], [4, [5, 6, [6], 6, 6, 6], 7]],

    ]
    for ev in evals:
        flat_list(ev)
        flat_list2(ev)
        flat_list3(ev)

    # import timeit
    # time = timeit.timeit('flat_list_lambda2([1,2,3])', setup='from __main__ import flat_list1')
    # time = timeit.timeit('flat_list([1,2,3])', globals=globals(), number=1)
