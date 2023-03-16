import sys

N = int(sys.stdin.readline().strip())
index = 0
answer = 1

while True:
    if answer >= N:
        print(index+1)
        break
    else:
        index += 1
        answer += index*6
