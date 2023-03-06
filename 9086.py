import sys
N = int(sys.stdin.readline().strip())

for __ in range(N):
    strings = sys.stdin.readline().strip()
    print(f"{strings[0]}{strings[-1]}")
    