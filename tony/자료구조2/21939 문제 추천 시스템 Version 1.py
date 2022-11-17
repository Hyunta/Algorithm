import heapq
import sys

input = sys.stdin.readline

n = int(input())
min_heap, max_heap = [], []
problems = dict()

for _ in range(n):
    num, lev = map(int, input().split())
    heapq.heappush(min_heap, [lev, num])
    heapq.heappush(max_heap, [-lev, -num])
    problems[num] = True

m = int(input())
for _ in range(m):
    operation = input().split()
    if operation[0] == "add":
        num, lev = int(operation[1]), int(operation[2])
        while not problems[-max_heap[0][1]]:
            heapq.heappop(max_heap)
        while not problems[min_heap[0][1]]:
            heapq.heappop(min_heap)
        problems[num] = True
        heapq.heappush(max_heap, [-lev, -num])
        heapq.heappush(min_heap, [lev, num])


    elif operation[0] == "solved":
        problems[int(operation[1])] = False

    elif operation[0] == "recommend":
        if operation[1] == '1':
            while not problems[-max_heap[0][1]]:
                heapq.heappop(max_heap)
            print(-max_heap[0][1])
        elif operation[1] == '-1':
            while not problems[min_heap[0][1]]:
                heapq.heappop(min_heap)
            print(min_heap[0][1])
