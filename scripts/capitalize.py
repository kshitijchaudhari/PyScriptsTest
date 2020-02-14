#!/bin/python3

def solve(s):
    name = s.split(" ")
    for i, element in enumerate(name):
        name[i] = str(name[i]).capitalize()
    m=" "
    return m.join(name)


if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)
