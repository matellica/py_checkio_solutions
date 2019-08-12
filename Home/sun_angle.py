#!/usr/bin/env checkio --domain=py run sun-angle
# https://py.checkio.org/mission/sun-angle/
# END_DESC
import re


def sun_angle(time):
    MINUTE_DEGREE = 180 / 720    # 0.25

    match = re.search(r'(\d+):(\d+)', time)
    hour = int(match.group(1))
    minutes = int(match.group(2))

    total_minutes = hour * 60 + minutes
    if total_minutes < (6 * 60) or total_minutes > (18 * 60):
        return "I don't see the sun!"
    else:
        return (total_minutes - (6 * 60)) * MINUTE_DEGREE


def sun_angle2(time):
    h, m = map(int, time.split(':'))
    # NOTE: 90: 15 * 6h
    #       m/4: 1/4=0.25, 60/4=15
    angle = 15 * h + m / 4 - 90
    return angle if 0 <= angle <= 180 else "I don't see the sun!"


def sun_angle3(time):
    return sun_angle3_lambda(time)

sun_angle3_lambda=lambda t:["I don't see the sun!",int(t[:2])*15+int(t[~1:])/4-90][6<=int(t[:2])+int(t[~1:])/60<=18]


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
    # test_checkio()
    for ans in map(sun_angle3,["01:23","12:15"]):
        print(ans)
