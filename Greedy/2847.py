n = int(input())
arr = []
ans = 0

for _ in range(n):
    arr.append(int(input()))

past = arr.pop()
for each in reversed(arr):
    if each >= past:
        ans += each - past + 1
        past = each - (each - past + 1)
    else:
        past = each

print(ans)