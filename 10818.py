import sys

N = int(sys.stdin.readline().strip())
A = [int(i) for i in sys.stdin.readline().strip().split(" ")]

print(f"{min(A)} {max(A)}")
