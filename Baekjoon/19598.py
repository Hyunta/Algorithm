import heapq
import sys

input = sys.stdin.readline

n = int(input())
meetings = [list(map(int, input().split())) for _ in range(n)]
meetings.sort()

heap = [0]
cnt = 1

for start, end in meetings:
    if start >= heap[0]:
        heapq.heappushpop(heap, end)
    else:
        cnt += 1
        heapq.heappush(heap, end)
print(cnt)

# for _ in range(n):
#     s, e = map(int, input().split())
#     meetings.append([s, 1])
#     meetings.append([e, -1])
# meetings.sort()
#
# cnt = 0
# maxRoom = 0
# for time, status in meetings:
#     cnt += status
#     if status == 1:
#         maxRoom = max(maxRoom, cnt)
#
# print(maxRoom)
