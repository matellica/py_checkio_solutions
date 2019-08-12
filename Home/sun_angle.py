#!/usr/bin/env checkio --domain=py run sun-angle
# https://py.checkio.org/mission/sun-angle/
# END_DESC
import re


def sun_angle(time):
    MINUTE_DEGREE = 180 / 720

    match = re.search(r'(\d+):(\d+)', time)
    hour = int(match.group(1))
    minutes = int(match.group(2))

    total_minutes = hour * 60 + minutes
    if total_minutes < (6 * 60) or total_minutes > (18 * 60):
        return "I don't see the sun!"
    else:
        return (total_minutes - (6 * 60)) * MINUTE_DEGREE


def test_checkio():
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("01:23") == "I don't see the sun!"
    assert sun_angle("5:59") == "I don't see the sun!"
    assert sun_angle("6:00") == 0
    assert sun_angle("07:00") == 15
    assert sun_angle("12:15") == 93.75
    assert sun_angle("12:30") == 97.5
    assert sun_angle("18:00") == 180
    print("Coding complete? Click 'Check' to earn cool rewards!")


if __name__ == '__main__':
    test_checkio()
