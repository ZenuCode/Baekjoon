count = 0

while True:
    count += 1
    res = 0
    l, p, v = map(int, input().split())
    if l == 0 and p == 0 and v == 0:
        break

    while v >= p:
        res += l
        v -= p
    
    
    if v > l:
        res += l
    else:
        res += v

    print("Case " + str(count) + ": " + str(res))

"""
import sys
input = sys.stdin.readline

case = 1
while True:
    l, p, v = map(int, input().split())
    if l == 0: break

    q, r = divmod(v, p)
    answer = q * l + min(l, r)
    
    print(f'Case {case}: {answer}')
    case += 1

"""
