import sys

input = sys.stdin.readline

n = int(input())
liquid = list(map(int, input().split()))
liquid.sort()

lt, rt = 0, n-1
res = liquid[n-1] ** 2
a = lt
b = rt

while lt < rt:
    tmp = liquid[lt] + liquid[rt]
    if abs(tmp) < res:
        a = lt
        b = rt
        if tmp == 0:
            break
        res = abs(tmp)
    if tmp >= 0:
        rt -= 1
    else:
        lt += 1
print(liquid[a], liquid[b])

