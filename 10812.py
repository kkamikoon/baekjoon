import sys

N, M = [int(i) for i in sys.stdin.readline().strip().split(" ")]
result = [i for i in range(N+1)]

for __ in range(M):
    begin, end, mid = [int(i) for i in sys.stdin.readline().strip().split(" ")]
    mid_to_end = result[mid:end+1]
    begin_to_mid = result[begin:mid]
    to_begin = result[:begin]
    from_end = result[end+1:]
    result = to_begin + mid_to_end + begin_to_mid + from_end

print(" ".join([str(i) for i in result[1:]]))
