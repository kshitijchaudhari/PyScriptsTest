def main():
    file = open("sample.txt", "r+")
    content = file.read()
    print(len(content))
    print(content)


main()
