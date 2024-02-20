a, b = list(map(int, input().split()))

arr = []
aCopy = a
numVal = 1

while aCopy != 1 and aCopy / 2 >= b:
    if aCopy % 2 == 1:
        arr.insert(0, numVal)
        aCopy -= 1
    aCopy = aCopy / 2
    numVal = numVal * 2

if aCopy != 1:
    while(aCopy != 0) :
        arr.insert(0, numVal)
        aCopy -= 1

print(arr)

indexOne = 0
indexTwo = 1
bottleCount = 0

while len(arr) != b:
    if arr[indexOne] == arr[indexTwo]:
        arr[indexOne] += arr[indexTwo]
        arr.pop(indexTwo)
        indexOne = 0
        indexTwo = 1
    elif indexTwo == len(arr) - 1:
        bottleCount += 1
        arr.append(1)
        indexOne = 0
        indexTwo = 1
    else:
        indexOne += 1
        indexTwo += 1

print(bottleCount)
