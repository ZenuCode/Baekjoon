import sys

exp = sys.stdin.readline().split('-')
num = []

for i in exp:
    sum, tmp = 0, i.split('+')
    for j in tmp:
        sum += int(j)
    num.append(sum)

n = num[0]
for i in range(1,len(num)):
    n -= num[i]

print(n)