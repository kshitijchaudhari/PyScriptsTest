def solution(x):
    arr = [i for i in x]
    result = []
    for i in arr:
        if i == " " or ord(i) < 97 or ord(i) > 122:
            result.append(i)
        elif ord(i) >= 97 or ord(i) <= 122:
            c = ord(i) - 97
            r = chr((122 - c))
            result.append(r)
    s = ""
    result = s.join(result)
    print(result)


solution("wrw blf hvv ozhg mrtsg'h vkrhlwv?")
solution("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!")