import sys

input = sys.stdin.readline
cnt = 0
for _ in range(int(input())):
    stack = []
    word = list(map(str, input().rstrip()))

    for x in word:
        if stack and x == stack[-1]:
            stack.pop()
        else:
            stack.append(x)
    if not stack:
        cnt += 1
print(cnt)
