import heapq
import sys

input = sys.stdin.readline
gas = []
for _ in range(int(input())):
    heapq.heappush(gas, list(map(int, input().split())))
goal, fuel = map(int, input().split())

move = []
cnt =0
while fuel < goal:
    while gas and gas[0][0] <= fuel:
        gs, f = heapq.heappop(gas)
        heapq.heappush(move, [-1*f, gs])

    if not move:
        cnt = -1
        break

    f, gs = heapq.heappop(move)
    fuel += -1 * f
    cnt += 1
print(cnt)

