import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    queue = list(map(int, input().split()))

    cnt = 0
    target = queue[m]
    queue[m] = -1

    while max(queue) > target:
        cnt += 1
        pop = queue.index(max(queue))
        queue = queue[pop+1:] + queue[:pop]

    print(cnt + queue[:queue.index(-1)].count(target) + 1)
