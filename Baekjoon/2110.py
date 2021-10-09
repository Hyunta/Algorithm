import sys

input = sys.stdin.readline

n, c = map(int, input().split())
house = []
for _ in range(n):
    house.append(int(input()))
house.sort()

lt = 1
rt = house[-1] - house[0]

while lt <= rt:
    mid = (lt + rt) // 2
    old = house[0]
    cnt = 1

    for i in range(1, len(house)):
        if house[i] >= old + mid:
            cnt += 1
            old = house[i]

    if cnt >= c:
        lt = mid + 1
    else:
        rt = mid - 1
print(rt)
