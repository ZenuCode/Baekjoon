import sys
input = sys.stdin.readline

n, A = int(input()), set(map(int, input().split()))
m, B = int(input()), list(map(int, input().split()))
res = ["1" if B_num in A else "0" for B_num in B]

print(*res)

# n = int(input())
# card_have = list(map(int, input().split()))
# card_have.sort()
# m = int(input())
# card_check = list(map(int, input().split()))
# res = []

# for each in card_check:
#     if each == card_have[0] or each == card_have[-1]:
#         res.append(1)
#         continue
#     else:
#         l, r = 0, len(card_have) - 1
#         found = False
#         while l <= r:
#             m = (l + r) // 2
#             if each == card_have[m]:
#                 res.append(1)
#                 found = True
#                 break
#             elif each < card_have[m]:
#                 r = m - 1
#             elif each > card_have[m]:
#                 l = m + 1
#         if not found:
#             res.append(0)

# print(*res)