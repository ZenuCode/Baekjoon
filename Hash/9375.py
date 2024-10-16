import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    wears = {}
    n = int(input())
    for _ in range(n):
        name, gear = input().strip().split()
        if gear in wears:
            wears[gear] += 1
        else:
            wears[gear] = 1
    
    cnt = 1
    for x in wears:
        cnt *= wears[x] + 1 #(1, 2, 3, or none) 
    
    print(cnt-1) # When everything is none