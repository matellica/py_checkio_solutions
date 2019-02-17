#!/usr/bin/env checkio --domain=py run most-wanted-letter

# https://py.checkio.org/mission/most-wanted-letter/


def checkio(text: str) -> str:

    text = text.lower()
    numbers = {}
    for char in text:
        if not char.isalpha():
            continue
        numbers[char] = numbers.get(char, 0) + 1

    maxkeys = [key[0] for key in numbers.items() if key[1] == max(numbers.values())]
    # res = max(numbers,key=numbers.get)
    maxkeys.sort()
    res = maxkeys.pop(0)
    return res


def test_checkio():
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")


if __name__ == '__main__':
    test_checkio()
