import sys

input = sys.stdin.readline
res = ""
s = input().rstrip().split("-")
for x in s:
    res += x[0]
print(res)