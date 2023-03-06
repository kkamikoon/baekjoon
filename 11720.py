import sys

N = int(sys.stdin.readline().strip())
numbers = [int(i) for i in list(sys.stdin.readline().strip())]
print(sum(numbers))