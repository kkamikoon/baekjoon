import sys
from collections import Counter

maximum = None
S = sys.stdin.readline().strip().upper()
count = Counter(S)

for k, v in count.most_common():
    if not maximum:
        maximum = k
    elif v == count[maximum]:
        maximum = "?"
        break
    elif v > count[maximum]:
        maximum = k

print(maximum)
