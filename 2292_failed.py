import sys

N = int(sys.stdin.readline().strip())
tmp = [1]
index = 0

while True:
    index += 1
    if N in tmp:
        print(index)
        break
    last = tmp[-1]
    tmp = [i for i in range(last+1, last+(index*6)+1)]


