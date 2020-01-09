def swap_case(s):
    m=[]
    for i in s:
        if i.islower():
            i=i.upper()
        elif i.isupper():
            i=i.lower()
        m.append(i)
        result=""
        for ele in m:
            result += ele
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)