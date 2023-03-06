import sys

N, X = [int(i) for i in sys.stdin.readline().strip().split(" ")]
A = [int(i) for i in sys.stdin.readline().strip().split(" ")]
result = []

for i in A:
    if i < X:
        result.append(str(i))
    
print(" ".join(result))