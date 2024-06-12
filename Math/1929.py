import sys
l, h = map(int, sys.stdin.readline().split())

for each in range(l, h + 1):
    if each == 1:
        continue

    for num in range(2, int(each ** 0.5) + 1):
        if each % num == 0:
            break
    
    else:
        print(each)
