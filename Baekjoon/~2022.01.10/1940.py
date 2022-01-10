import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
parts = list(map(int, input().split()))
parts.sort()
lt = 0
rt = n - 1
cnt = 0

while lt < rt:
    tmp = parts[lt] + parts[rt]
    if tmp < m:
        lt += 1
    elif tmp == m:
        cnt += 1
        lt += 1
        rt -= 1
    else:
        rt -= 1
print(cnt)
