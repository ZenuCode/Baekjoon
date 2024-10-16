import sys
input = sys.stdin.readline


mens, party =list(map(int,input().split()))
cnt =0

know = set(input().split()[1:])
rounge = []
for i in range(party):
    rounge.append(set(input().split()[1:]))
    
for _ in range(party):
    for j in rounge:
        if j & know:
            know = know.union(j)

for j in rounge:
    if j & know:
        continue
    cnt +=1
print(cnt)