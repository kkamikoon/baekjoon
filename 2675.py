import sys

T = int(sys.stdin.readline().strip())

for __ in range(T):
    R, S = sys.stdin.readline().strip().split(" ")
    print("".join([s*int(R) for s in list(S)]))

