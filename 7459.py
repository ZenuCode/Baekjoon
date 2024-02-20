import sys
"""
n = num of values
l = starting number
k = number of outputs
m = number of last digits used
"""
n, l, k ,m = map(int, sys.stdin.readline().rstrip().split())
coeff = []
for i in range(n + 1):
    coeff.append(sys.stdin.readline().rstrip())

print(n, l, k, m)
print(coeff)

for i in range(k):
    