def main():
    file = open("../assets/sample.txt", "r+")
    content = file.read()
    print(len(content))
    print(content)


main()
