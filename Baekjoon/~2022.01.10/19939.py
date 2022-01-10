import sys

input = sys.stdin.readline


def solution():
    n, k = map(int, input().split())
    min_sum = k * (k + 1) // 2
    if min_sum > n:
        return -1
    if (n - min_sum) % k == 0:
        return k - 1
    else:
        return k

print(solution())
