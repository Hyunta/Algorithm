import sys

input = sys.stdin.readline
a, i = list(map(int, input().split()))
print((i - 1) * a + 1)
