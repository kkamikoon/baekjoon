import sys

def reverse(array, i, j):
    tmp = array[i:j+1]
    tmp.reverse()

    for index in range(i, j+1):
        array[index] = tmp[index-i]

    return array

N, M = [int(i) for i in sys.stdin.readline().strip().split(" ")]
bucket = [i for i in range(N+1)]

for __ in range(M):
    i, j = [int(i) for i in sys.stdin.readline().strip().split(" ")]
    bucket = reverse(bucket, i, j)

print(" ".join([str(i) for i in bucket[1:]]))
