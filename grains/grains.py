def square(number):
    m = {i: 2**i for i in range(64)}
    if 1 <= number <= 64:
        return m[number-1]
    else:
        raise ValueError("square must be between 1 and 64")


def total():
    return sum([2**i for i in range(64)])
