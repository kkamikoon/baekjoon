import sys

# Initialization
w, h = 10, 10
paper = []

for __ in range(100):
    paper.append([0 for __ in range(100)])

# Solve
N = int(sys.stdin.readline().strip())

for __ in range(N):
    x, y = [int(i) for i in sys.stdin.readline().strip().split(" ")]

    for _w in range(w):
        for _h in range(h):
            paper[x+_w-1][_h+y-1] = 1
total = 0

for p in paper:
    # print(" ".join([str(_p) for _p in p]))
    total += sum(p)

print(total)
    
