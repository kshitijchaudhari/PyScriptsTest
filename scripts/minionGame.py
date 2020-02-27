
def wordcreation(input):
    words = []
    for e, i in enumerate(input):
        text =""
        for a in input[e:]:
            text = text + a
            words.append(text)
    StuartScore = 0
    KevinScore = 0
    for m in words:
        if m[0:1] in ["A", "E", "I", "O", "U"]:
            KevinScore = KevinScore + 1
        else:
            StuartScore = StuartScore + 1
    if KevinScore>StuartScore:
        print("Kevin ", KevinScore)
    elif StuartScore>KevinScore:
        print("Stuart ", StuartScore)
    else:
        print("Draw")


wordcreation("BANANA")