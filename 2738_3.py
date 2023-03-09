import sys

N, M = [int(i) for i in sys.stdin.readline().strip().split(" ")]

A = []
B = []
R = []

for __ in range(N):
    A.append([int(i) for i in sys.stdin.readline().strip().split(" ")])

for __ in range(N):
    B.append([int(i) for i in sys.stdin.readline().strip().split(" ")])

for a, b in zip(A, B):
    tmp = []
    for _a, _b in zip(a, b):
        tmp.append(_a+_b)

    R.append(tmp)

for r in R:
    print(" ".join([str(i) for i in r]))

