import sys
import itertools

N = int(sys.stdin.readline().strip())
area = []
indexes = []
width, height = 10, 10

for __ in range(N):
    indexes.append([int(i) for i in sys.stdin.readline().strip().split(" ")])

def get_intersection_area(index1, index2):
    if index1[0] > index2[0] + width:
        return 0
    elif index1[0] + width < index2[0]:
        return 0
    elif index1[1] > index2[1] + height:
        return 0
    elif index1[1] + height < index2[1]:
        return 0
    
    x = max(index1[0], index2[0])
    y = max(index1[1], index2[1])
    w = min(index1[0] + width, index2[0] + width) - x
    h = min(index1[1] + height, index2[1] + height) - y

    return w * h

for i1, i2 in itertools.combinations(indexes, 2):
    area.append(get_intersection_area(i1, i2))

print((width*height)*N - sum(area))