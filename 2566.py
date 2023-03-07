import sys

matrix = []
_max = 0

for __ in range(9):
    matrix.append([int(i) for i in sys.stdin.readline().strip().split(" ")])

for m in matrix:
    if _max < max(m):
        _max = max(m)

for i, m in enumerate(matrix):
    if _max in m:
        print(_max)
        print(f"{i+1} {m.index(_max)+1}")
        break

