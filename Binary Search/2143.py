import sys
input = sys.stdin.readline

target = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

def find_sums(arr):
    sumArr = []
    for start in range(len(arr)):
        currSum = 0
        for end in range(start, len(arr)):
            currSum += arr[end]
            sumArr.append(currSum)
    
    return sumArr

def find_sum_count(arr):
    sumMap = {}
    for each in arr:
        if each in sumMap:
            sumMap[each] += 1
        else:
            sumMap[each] = 1
    
    return sumMap

def problem_2143():
    res = 0
    arrA = find_sums(a)
    arrB = find_sums(b)

    mapA = find_sum_count(arrA)
    mapB = find_sum_count(arrB)

    for eachA in mapA:
        findNum = target - eachA
        if findNum in mapB:
            res += mapA[eachA] * mapB[findNum]
    
    return res

print(problem_2143())