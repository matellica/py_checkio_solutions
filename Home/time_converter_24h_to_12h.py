#!/usr/bin/env checkio --domain=py run time-converter-24h-to-12h
# https://py.checkio.org/mission/time-converter-24h-to-12h/

import re


def time_converter(time):
    match = re.search(r'(\d+):(\d+)', time)
    hour = int(match.group(1))
    minute = match.group(2)

    if hour == 0:
        hour = 12
        period = 'a.m.'
    elif hour == 12:
        period = 'p.m.'
    elif hour > 12:
        hour = hour - 12
        period = 'p.m.'
    else:
        period = 'a.m.'
    return '{0}:{1} {2}'.format(hour, minute, period)


def test_time_converter():
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('00:30') == '12:30 a.m.'
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")


if __name__ == '__main__':
    test_time_converter()
