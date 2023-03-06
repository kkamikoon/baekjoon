A = int(input())
B = int(input())
R = A*B
nums = []

while B:
    nums.append(B%10)
    B = int(B/10)

for num in nums:
    print(A*num)
print(R)
