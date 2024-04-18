import heapq
INF = int(1e9)

n, k = map(int, input().split())

q = [(0, k)]
while q :
    time, now = heapq.heappop(q)
    
    if now == n :
        print(time)
        break
    
    if now < 0 :
        continue
    elif now < n :
        heapq.heappush(q, (time + n - now, n))
    elif now % 2 == 0 :
        heapq.heappush(q, (time, now // 2))  # 텔레포트
        heapq.heappush(q, (time + now - n, n))
    else :
        heapq.heappush(q, (time + 1, now + 1))
        heapq.heappush(q, (time + 1, now - 1))