import sys
import heapq

input = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n):
    tmp = int(input())
    if tmp == 0 and heap:
        print(heapq.heappop(heap)[1])
    elif tmp == 0 and not heap:
        print(0)
    else:
        heapq.heappush(heap, [abs(tmp), tmp])

