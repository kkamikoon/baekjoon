import sys

N, M = [int(i) for i in sys.stdin.readline().strip().split(" ")]
bucket = [0 for __ in range(N)]

for m in range(M):
    i, j, k = [int(i) for i in sys.stdin.readline().strip().split(" ")]

    for index in range(i-1, j):
        bucket[index] = k

print(" ".join([str(b) for b in bucket]))
