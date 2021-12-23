import heapq
import sys

input = sys.stdin.readline

n = int(input())
lecture_info = [list(map(int, input().split())) for _ in range(n)]
lecture_info.sort(key=lambda x: x[1])

total_room = [-1]
min_room = -1
for lecture in lecture_info:
    end_time = heapq.heappop(total_room)
    if lecture[1] < end_time:
        heapq.heappush(total_room, end_time)
    heapq.heappush(total_room, lecture[2])
    min_room = max(min_room, len(total_room))

print(min_room)
