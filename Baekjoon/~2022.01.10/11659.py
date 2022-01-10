import sys

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
prefix_sum = [0]
tmp = 0
for num in nums:
    tmp += num
    prefix_sum.append(tmp)

for _ in range(m):
    i, j = map(int, input().split())
    print(prefix_sum[j] - prefix_sum[i-1])
