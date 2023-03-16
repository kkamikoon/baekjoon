import sys
import itertools

N = int(sys.stdin.readline().strip())
done = False
width, height = 10, 10
rectangles = []
answer = (width*height)*N
repeated = 1

def get_intersection_area(r1, r2):
    # x: 0, y: 1, w: 2, h: 3
    if r1[0] > r2[0] + r2[2]:
        return None, 0
    elif r1[0] + r2[2] < r2[0]:
        return None, 0
    elif r1[1] > r2[1] + r2[3]:
        return None, 0
    elif r1[1] + r1[3] < r2[1]:
        return None, 0
    
    x = max(r1[0], r2[0])
    y = max(r1[1], r2[1])
    w = min(r1[0] + r1[2], r2[0] + r2[2]) - x
    h = min(r1[1] + r1[3], r2[1] + r2[3]) - y

    return [(x, y, w, h), w*h]

for __ in range(N):
    # x, y, w, h
    rectangles.append([int(i) for i in sys.stdin.readline().strip().split(" ")] + [width, height])

if N == 1:
    print(width * height)
else:
    while not done:
        _tmp = []

        if len(rectangles) <= 1:
            done = True
            break

        for r1, r2 in itertools.combinations(rectangles, 2):
            rect, area = get_intersection_area(r1, r2)

            if not rect:
                continue

            if repeated % 2:
                answer -= area
            else:
                answer += area

            _tmp.append(rect)

        rectangles = _tmp

    print(answer)