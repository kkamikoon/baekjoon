import sys

A = []

for i in range(9):
    A.append(int(sys.stdin.readline().strip()))

print(max(A))
print(A.index(max(A))+1)