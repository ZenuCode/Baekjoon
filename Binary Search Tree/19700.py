import sys
from bisect import bisect, bisect_left
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
students = []
teams = []
for _ in range(N):
    students.append(tuple(map(int, input().rstrip().split())))

students = sorted(students, key=lambda x: -x[0])

for h, k in students:
    if k == 1 or len(teams) == 0:
        teams.append(-1)
        continue

    t = bisect_left(teams, -1*(k-1))
    if t >= len(teams):
        teams.append(-1)
    else:
        teams[t] -= 1

print(len(teams))