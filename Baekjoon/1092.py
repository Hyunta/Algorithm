import sys

input = sys.stdin.readline

n = int(input())
crane = list(map(int, input().split()))
m = int(input())
boxes = list(map(int, input().split()))

if max(crane) < max(boxes):
    print(-1)
    exit()

crane.sort(reverse=True)
boxes.sort(reverse=True)

time = 0
checked = [False] * m
cnt = 0

position = [0] * n

while cnt < len(boxes):
    for i in range(n):
        while position[i] < len(boxes):
            if not checked[position[i]] and crane[i] >= boxes[position[i]]:
                checked[position[i]] = True
                position[i] += 1
                cnt += 1
                break
            position[i] += 1
    time += 1
print(time)
