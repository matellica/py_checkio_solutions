#!/usr/bin/env checkio --domain=py run flatten-list
# https://py.checkio.org/mission/flatten-list/
# END_DESC
import util


@util.measure
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


@util.measure
def flat_list2(array):
    return flat_list2_lambda(array)


flat_list2_lambda=f=lambda d:[d]if int==type(d)else sum(map(f,d),[])


@util.measure
def flat_list3(l):
    r = []
    def f(l):
        for i in l:
            r.append(i) if type(i) is int else f(i)
    f(l)
    return r


@util.measure
def flat_list4(a):
    return eval('['+str(a).replace('[','').replace(']','')+']')


@util.measure
def flat_list5(l):
    return flat_list5_lambda(l)

flat_list5_lambda=lambda array: eval('['+str(array).translate(str.maketrans('','','[]'))+']')


@util.measure
def flat_list6(array: list) -> list:
    from itertools import chain

    return list(
        chain(
            *(flat_list(i) if type(i) is list else (i,) for i in array)
        )
    )


def test_checkio():
    assert flat_list([1, 2, 3]) == [1, 2, 3], "First"
    assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "Second"
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "Third"
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "Four"
    print('Done! Check it')


if __name__ == '__main__':
    # test_checkio()
    evals = [
        [-1, [1, [-2], 1], -1],
        [1, [2, 2, 2], 4],
        [[[2]], [4, [5, 6, [6], 6, 6, 6], 7]],

    ]
    for ev in evals:
        flat_list(ev)
        flat_list2(ev)
        flat_list3(ev)
        flat_list4(ev)
        flat_list5(ev)
        flat_list6(ev)
        util.print_scores()

    # import timeit
    # time = timeit.timeit('flat_list_lambda2([1,2,3])', setup='from __main__ import flat_list1')
    # time = timeit.timeit('flat_list([1,2,3])', globals=globals(), number=1)
