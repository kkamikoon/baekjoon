import sys

N, M = [int(i) for i in sys.stdin.readline().strip().split(" ")]

A = []
B = []
R = []

for __ in range(N):
    A.append([int(i) for i in sys.stdin.readline().strip().split(" ")])

for __ in range(N):
    B.append([int(i) for i in sys.stdin.readline().strip().split(" ")])

for n in range(N):
    tmp = []
    for m in range(M):
        tmp.append(A[n][m] + B[n][m])

    R.append(tmp)

for r in R:
    print(" ".join([str(i) for i in r]))

