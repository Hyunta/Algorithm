import heapq
import sys
from collections import defaultdict


def input():
    return sys.stdin.readline().rstrip()


t = int(input())
for _ in range(t):
    k = int(input())
    min_heap = []
    max_heap = []
    total_ele_cnt = 0
    ele_cnt = defaultdict(int)

    for _ in range(k):
        operator, num = input().split()
        num = int(num)

        if operator == "I":
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
            total_ele_cnt += 1
            ele_cnt[num] += 1

        elif operator == "D":
            if total_ele_cnt <= 0:
                continue
            if num == 1:
                while True:
                    del_num = -heapq.heappop(max_heap)
                    if ele_cnt[del_num] != 0:
                        ele_cnt[del_num] -= 1
                        break
            elif num == -1:
                while True:
                    del_num = heapq.heappop(min_heap)
                    if ele_cnt[del_num] != 0:
                        ele_cnt[del_num] -= 1
                        break
            total_ele_cnt -= 1

    if total_ele_cnt <= 0:
        print("EMPTY")
    else:
        while True:
            max_v = -heapq.heappop(max_heap)
            if ele_cnt[max_v] != 0:
                break
        while True:
            min_v = heapq.heappop(min_heap)
            if ele_cnt[min_v] != 0:
                break
        print(max_v, min_v)
