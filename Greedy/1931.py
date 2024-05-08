import sys
input = sys.stdin.readline

n = int(input())
meeting_times = [list(map(int, input().split())) for _ in range(n)]
meeting_times = sorted(meeting_times, key = lambda x : (x[1], x[0]))

count = 1
end_time = meeting_times[0][1]
for i in range(1, n):
    if (meeting_times[i][0] >= end_time):
        end_time = meeting_times[i][1]
        count += 1

print(count)