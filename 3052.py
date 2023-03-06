import sys
result = []

for __ in range(10):
    result.append(int(sys.stdin.readline().strip()) % 42)

print(len(set(result)))