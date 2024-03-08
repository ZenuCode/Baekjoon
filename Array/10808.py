text = input()
arr = [0] * 26

for i in text:
    arr[ord(i) - 97] += 1

print(*arr)