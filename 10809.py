import sys
from string import ascii_lowercase

alpha = {c: -1 for c in list(ascii_lowercase)}
S = list(sys.stdin.readline().strip())

for k, v in alpha.items():
    if v == -1:
        try:
            alpha[k] = S.index(k)
        except:
            pass

print(" ".join([str(i) for i in alpha.values()]))

