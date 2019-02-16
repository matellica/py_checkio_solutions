#!/usr/bin/env checkio --domain=py run house-password
# https://py.checkio.org/mission/house-password/

import re


def checkio(password):
    if not (0 < len(password) <= 64):
        return False
    if (len(password) < 10):
        return False
    if not (re.match("[a-zA-Z0-9]+", password)):
        return False
    if not (re.search(r'[0-9]+', password)):
        return False
    if not (re.search(r'[A-Z]+', password)):
        return False
    if not (re.search(r'[a-z]+', password)):
        return False
    return True


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
