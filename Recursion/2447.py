# import sys
# sys.setrecursionlimit(10**6)

# n = int(sys.stdin.readline().rstrip())
# graph = [[" " for _ in range(n)] for _ in range(n)]

# def recur(x, y, m):
#     if m == 3:
#         graph[x][y] = "*"
#         graph[x][y + 1] = "*"
#         graph[x][y + 2] = "*"
#         graph[x + 1][y] = "*"
#         graph[x + 1][y + 2] = "*"
#         graph[x + 2][y] = "*"
#         graph[x + 2][y + 1] = "*"
#         graph[x + 2][y + 2] = "*"
#     else:
#         recur(x, y, m//3)
#         recur(x, y + (m//3), m//3)
#         recur(x, y + (m//3)*2, m//3)
#         recur(x + (m//3), y, m//3)
#         #recur(x + (m//3), y + (m//3), m//3)
#         recur(x + (m//3), y + (m//3)*2, m//3)
#         recur(x + (m//3)*2, y, m//3)
#         recur(x + (m//3)*2, y + (m//3), m//3)
#         recur(x + (m//3)*2, y + (m//3)*2, m//3)
#     return

# recur(0, 0, n)
# for i in range(n):
#     for j in range(n):
#         print(graph[i][j], end='')
#     print()


def star_print(n):
    if n == 1:
      return ["*"]
    star = star_print(n//3)
    ans = []
    for i in star:
      ans.append(i * 3)
    for i in star:
      ans.append(i + " " * (n//3) + i)
    for i in star:
      ans.append(i * 3) 

    return ans

n = int(input())  
print("\n".join(star_print(n)))