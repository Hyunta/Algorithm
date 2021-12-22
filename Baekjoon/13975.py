import heapq
import sys

input = sys.stdin.readline

test_cnt = int(input())
for _ in range(test_cnt):
    chapter_cnt = int(input())
    pages = list(map(int, input().split()))
    heapq.heapify(pages)
    cost = 0
    for _ in range(chapter_cnt-1):
        least_page_1 = heapq.heappop(pages)
        least_page_2 = heapq.heappop(pages)
        heapq.heappush(pages, least_page_1 + least_page_2)
        cost += least_page_1 + least_page_2
    print(cost)
