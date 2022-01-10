import sys

input = sys.stdin.readline

arr = list(map(str, input().rstrip()))
stack = []
cnt = 0

for i in range(len(arr)):
    x = arr[i]
    if x == '(':
        stack.append(x)
    elif x == ')':
        tmp = stack.pop()
        if arr[i-1] == '(':
            cnt += len(stack)
        else:
            cnt += 1
print(cnt)
