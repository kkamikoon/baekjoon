import sys

done = False
N, M = [int(i) for i in sys.stdin.readline().strip().split(" ")]
T1 = []
T2 = []
result = []

while not done:
    tmp = sys.stdin.readline().strip()

    if not tmp:
        break

    tmp = [int(i) for i in tmp.split(" ")]
    T1 += tmp

A = T1[int(len(T1)/2):]
B = T1[:int(len(T1)/2)]
    
for a, b in zip(A, B):
    T2.append(a+b)

while T2:
    result.append(T2[:M])
    del T2[:M]

for r in result:
    print(" ".join([str(i) for i in r]))
