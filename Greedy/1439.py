arr = list(map(str, input().strip()))
count = 0
switched = False
curr = arr[0]

for each in arr:
    if each != curr and not switched:
        switched = True
        curr = each
        count += 1
    elif each != curr and switched:
        switched = False
        curr = each

print(count)    