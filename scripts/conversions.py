def print_formatted(number):
    for i in range(1, number + 1):
        print(str(i) + " " + str(oct(i)).replace("0o", "") + " " + str(hex(i)).replace("0x", "") + " " + str(bin(i)).replace("0b", ""))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
