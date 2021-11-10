import sys

input = sys.stdin.readline

s = input().rstrip()

for i in range(len(s)//2):
    if s[i] != s[-i-1]:
        print(0)
        break
else:
    print(1)