import re

c = input()
z = re.findall(r'[AEIOUaeiou]{2,100}[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM]', c)
if len(z) > 0:
    for v in z:
        print(v[:-1])
else:
    print("-1")
