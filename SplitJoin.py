def split_and_join(line):
    m = line.split(" ")
    n = "-".join(m)
    return n

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)