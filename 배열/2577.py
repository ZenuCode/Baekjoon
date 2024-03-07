num = 1
ans = [0] * 10

for _ in range(3):
    num = int(input()) * num

arr = list(map(int, str(num)))

for i in arr:
    ans[i] += 1

for j in ans:
    print(j)

"""
A = int(input())
B = int(input())
C = int(input())
num=str(A*B*C)

for x in range(10):
    print(num.count(str(x)))
"""