import sys
input = sys.stdin.readline

n, k = map(int, input().split())
pokeName = {}
pokeIndex = {}
for i in range(1, n+1):
    name = input().rstrip()
    pokeName[name] = i
    pokeIndex[str(i)] = name

for j in range(k):
    check = input().rstrip()
    if 48 <= ord(check[0]) <= 57:
        print(pokeIndex[check])
    else:
        print(pokeName[check])
