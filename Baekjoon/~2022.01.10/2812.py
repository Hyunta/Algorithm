import sys

input = sys.stdin.readline

n, k = map(int, input().split())
nums = list(map(str, input().rstrip()))

res = []
cnt = k

for i in range(n):
    while cnt > 0 and res:
        if res[len(res) - 1] < nums[i]:
            res.pop()
            cnt -= 1
        else:
            break
    res.append(nums[i])

for i in range(n - k):
    print(res[i], end="")
