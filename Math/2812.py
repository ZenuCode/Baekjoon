N,K = map(int,input().split())
s = input()

arr = []
for word in s:
    print("New Line")
    print(word)
    print(arr)
    print(K)
    while arr and int(arr[-1]) < int(word) and K>0:
        print("If")
        print(int(arr[-1]))
        print(word)
        arr.pop()
        K -= 1
    arr.append(word)


if K>0:
    print(''.join(map(str,arr[:-K])))
    print("Why")
else:
    print(''.join(map(str,arr)))