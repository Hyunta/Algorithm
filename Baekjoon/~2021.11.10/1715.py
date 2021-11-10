import heapq
import sys

input = sys.stdin.readline

n = int(input())
cards = []
for _ in range(n):
    heapq.heappush(cards, int(sys.stdin.readline()))

if len(cards) == 1:
    print(0)
else:
    answer = 0
    while len(cards) > 1:
        tmp1 = heapq.heappop(cards)
        tmp2 = heapq.heappop(cards)
        answer += tmp1 + tmp2
        heapq.heappush(cards, tmp1 + tmp2)

    print(answer)