import sys

N = int(sys.stdin.readline())

for __ in range(N):
    A = [int(i) for i in sys.stdin.readline().strip().split(" ")]
    students = A[0]
    scores = A[1:]
    average = sum(scores) / students

    successes = sum([1 if i > average else 0 for i in scores])
    print(f"{(successes / students)*100:.3f}%")
