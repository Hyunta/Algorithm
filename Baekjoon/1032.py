import sys

input = sys.stdin.readline
n = int(input())
pattern = input().rstrip()
for _ in range(n - 1):
    tmp_pattern = input().rstrip()
    for i in range(len(tmp_pattern)):
        if pattern[i] != tmp_pattern[i]:
            pattern = pattern[:i] + "?" + pattern[i+1:]
print(pattern)
