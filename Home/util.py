from decimal import Decimal
import time
import random
import string

scores = {}


def measure(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        exec_time = "{0:.10f}".format(Decimal(end_time - start_time))
        scores[func.__name__] = exec_time
        # print(f'{func.__name__}: {exec_time}')
        return result
    return wrapper


def print_scores():
    for idx, score in enumerate(sorted(scores.items(), key=lambda x: x[1]), 1):
        print(f'{idx}** {score[0]}: {score[1]}')
    print('----------------------------------------')


def random_string(n):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=n))
