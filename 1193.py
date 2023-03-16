import sys

N = int(sys.stdin.readline().strip())
i = 1
a = 1

if N == 1:
    print("1/1")
else:
    while True:
        if a >= N:
            if i % 2:
                m = (2*i)-N+1
                c = i+1-m
                print(f"{c}/{m}")
            else:
                m = (2*(i+1))-N+1
                c = i+1-m
                print(f"{c}/{m}")
                
            break
        else:
            a += (i+1)
            i += 1
            