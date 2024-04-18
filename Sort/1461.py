import sys

total, carry = map(int, sys.stdin.readline().rstrip().split())
arr = sorted(list(map(int, sys.stdin.readline().rstrip().split())))
pos = [x for x in arr if x > 0]
neg = [x for x in arr if x < 0]

pos.sort(reverse=True)
steps = []
for i in range(0, len(pos), carry):
    steps.append(pos[i])
for i in range(0, len(neg), carry):
    steps.append(-neg[i])

steps.sort(key= lambda x: abs(x))
print(steps[-1] + sum(steps[:-1]) * 2)