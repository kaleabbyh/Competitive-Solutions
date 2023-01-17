
def flatten(iterable):
    a = []
    for i in iterable:
        if type(i) == list or type(i) == tuple:
            a.extend(flatten(i))
        elif i is not None:
            a.append(i)

    return a
