# noinspection PyPep8Naming
def calculateScore(fileOrString, isFile=False):
    if isFile:
        with open(fileOrString, 'r') as file:
            s = file.read().replace('\n', '')
    else:
        s = fileOrString
    stringLength = len(s)
    KevinScore = 0
    StuartScore = 0
    for i, j in enumerate(s):
        count = stringLength - i
        if j[0:1] in ["A", "E", "I", "O", "U"]:
            KevinScore = KevinScore + count
        else:
            StuartScore = StuartScore + count
    if KevinScore > StuartScore:
        print("Kevin", KevinScore)
    elif StuartScore > KevinScore:
        print("Stuart", StuartScore)
    else:
        print("Draw")


# Calling Format
# calculateScore('File Name with Path', True for File)
# calculateScore("String to parse")

calculateScore('../assets/largeString', True)
calculateScore("BANANA")
