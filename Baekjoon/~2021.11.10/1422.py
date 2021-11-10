import sys
from functools import cmp_to_key

input = sys.stdin.readline


def cmp(x, y):
    if str(x) + str(y) > str(y) + str(x):
        return -1
    else:
        return 1


k, n = map(int, input().split())
arr = [int(input()) for _ in range(k)]
arr.sort(reverse=True)
for _ in range(k, n):
    arr.append(arr[0])
arr.sort(key=cmp_to_key(cmp))
for i in arr:
    print(i, end='')
