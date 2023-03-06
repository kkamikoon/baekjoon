import sys

N = int(sys.stdin.readline().strip())
M = [int(i) for i in sys.stdin.readline().strip().split(" ")]
result = []

for m in M:
    result.append(m / max(M) * 100)

print(sum(result) / N)
