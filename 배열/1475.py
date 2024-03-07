num = input()
arr = [0] * 10
for i in num:
    if i == "9":
        i = "6"
    arr[int(i)] += 1
arr[6] = (arr[6] + 1) // 2
print(max(arr))