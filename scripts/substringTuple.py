import re

S = "aaadaa"
k = "aa"
f = [m.start() for m in re.finditer('(?='+k+')', S)]
g = [m.end() for m in re.finditer('('+k+'=?)', S)]
print(f)
print(g)