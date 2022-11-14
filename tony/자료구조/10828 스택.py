import sys

input = sys.stdin.readline

n = int(input())
stack = []

for i in range(n):
    val = input().split()
    oper = val[0]

    if oper == "push":
        stack.append(int(val[1]))

    if oper == "top":
        if not stack:
            print(-1)
        else:
            print(stack[-1])

    if oper == "size":
        print(len(stack))

    if oper == "empty":
        if not stack:
            print(1)
        else:
            print(0)

    if oper == "pop":
        if not stack:
            print(-1)
        else:
            print(stack.pop(-1))
