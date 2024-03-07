text1 = input()
text2 = input()

arr = [0] * 26
ans = 0

for i in text1:
    arr[ord(i) - 97] += 1

for j in text2:
    arr[ord(j) - 97] -= 1

for k in arr:
    ans += abs(k)

print(ans)