import sys

input = sys.stdin.readline
for _ in range(int(input())):
    l = input().rstrip()
    lt, rt = [], []
    for x in l:
        if x == '<':
            if lt:
                rt.append(lt.pop())
        elif x == '>':
            if rt:
                lt.append(rt.pop())
        elif x == '-':
            if lt:
                lt.pop()
        else:
            lt.append(x)
    rt.reverse()
    result = lt + rt
    print(''.join(result))


