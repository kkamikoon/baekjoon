import sys

students = [i+1 for i in range(30)]

for __ in range(28):
    del students[students.index(int(sys.stdin.readline().strip()))]

students.sort()

print(students[0])
print(students[1])

