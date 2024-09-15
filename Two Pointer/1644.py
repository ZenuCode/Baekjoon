import math

def sieve_of_eratosthenes(n):
    prime = [True for i in range(num+1)]
    p = 2

    while (p * p <= num):
        if (prime[p] == True):
            for i in range(p * p, num+1, p):
                prime[i] = False
        p += 1
 
    for p in range(2, num+1):
        if prime[p]:
            print(p)
            
    return [i for i in range(2, n + 1) if prime[i]]

num = int(input())
sumArr = sieve_of_eratosthenes(num)

l, r = 0, 0
currSum = 0
res = 0

while r <= len(sumArr):
    if currSum < num:
        if r != len(sumArr):
            currSum += sumArr[r]
        r += 1
    elif currSum > num:
        currSum -= sumArr[l]
        l += 1
    else:
        res += 1
        if r != len(sumArr):
            currSum += sumArr[r]
        r += 1

print(res)