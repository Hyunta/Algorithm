import sys

input = sys.stdin.readline

n, k = map(int, input().split())

res = 0
while bin(n).count('1') > k:
    plus = 2 ** (bin(n)[::-1].index('1'))
    res += plus
    n += plus
print(res)
