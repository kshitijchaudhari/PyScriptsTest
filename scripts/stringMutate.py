def mutate_string(string, position, character):
    m = list(string)
    m[position] = character
    r = "".join(m)
    return r

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)