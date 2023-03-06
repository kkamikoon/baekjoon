import sys

N = int(sys.stdin.readline())
nums = [int(i) for i in sys.stdin.readline().strip().split(" ")]
v = int(sys.stdin.readline())

print(nums.count(v))


