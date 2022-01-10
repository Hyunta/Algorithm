# 양수 = 산성 , 음수 = 알칼리성
import sys

input = sys.stdin.readline

n = int(input())
liquids = list(map(int, input().split()))
liquids.sort()
lt, rt = 0, n-1
near_zero = liquids[lt] + liquids[rt]
res1 = liquids[lt]
res2 = liquids[rt]

while lt < rt:
    tmp = liquids[lt] + liquids[rt]
    if abs(tmp) < abs(near_zero):
        near_zero = tmp
        res1 = liquids[lt]
        res2 = liquids[rt]
        if tmp == 0:
            break
    if tmp < 0:
        lt += 1
    else:
        rt -= 1
print(res1, res2)

