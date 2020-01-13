if __name__ == '__main__':
    s = input()
    alphanum = False
    alpha = False
    digit = False
    lower = False
    upper = False
    for _ in list(s):
        if str(_).isupper():
            upper = True
        if str(_).islower():
            lower = True
        if str(_).isalnum():
            alphanum = True
        if str(_).isalpha():
            alpha = True
        if str(_).isdigit():
            digit = True
    print(alphanum)
    print(alpha)
    print(digit)
    print(lower)
    print(upper)


