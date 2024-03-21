n, r, c = map(int, input().split())
ans = 0
while n != 0:
    n -= 1
    if r < 2**n and c < 2**n:
        ans += 0
    elif r < 2**n and c >= 2**n:
        ans += (4**n)
        c -= 2**n
    elif r >= 2**n and c < 2**n:
        ans += (4**n)*2
        r -= 2**n
    else:
        ans += (4**n)*3
        c -= 2**n
        r -= 2**n
    
print(ans)