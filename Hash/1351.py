n, p, q = map(int, input().split())
memo = {}
memo[0] = 1

def search(val):
    if val in memo:
        return memo[val]

    memo[val] = search(val // p) + search(val // q)
    return memo[val]

if n != 0:
    search(n)
print(memo[n])