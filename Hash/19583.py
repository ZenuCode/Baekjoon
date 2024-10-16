import sys
input = sys.stdin.readline

start, end, finish = input().strip().split()
start = int("".join(start.split(':')))
end = int("".join(end.split(':')))
finish = int("".join(finish.split(':')))


classMap = {}
res = 0

while True:
    try:
        time, name = input().strip().split()
        time = int("".join(time.split(':')))

        if time <= start:
            classMap[name] = True
        elif end <= time <= finish and name in classMap:
            del classMap[name]
            res += 1
        elif time > finish:
            break
    except:
        break

print(res)