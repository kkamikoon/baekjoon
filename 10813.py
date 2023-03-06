import sys

N, M = [int(i) for i in sys.stdin.readline().strip().split(" ")]
bucket = [i for i in range(N+1)]

for __ in range(M):
    A, B = [int(i) for i in sys.stdin.readline().strip().split(" ")]
    
    T = bucket[A]
    bucket[A] = bucket[B]
    bucket[B] = T

print(" ".join([str(i) for i in bucket[1:]]))
