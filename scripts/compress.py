import itertools

if __name__ == '__main__':
    s = input()
    items = itertools.groupby(s)
    op = ""
    for key, grp in items:
        op = op + "({}, {}) ".format(len(list(grp)), key)
    print(op)
