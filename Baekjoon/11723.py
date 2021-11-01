import sys

input = sys.stdin.readline

s = set()
for _ in range(int(input())):
    tmp = input().strip().split()

    if len(tmp) == 1:
        if tmp[0] == "all":
            s = set([i for i in range(1, 21)])
        else:
            s = set()
    else:
        func, val = tmp[0], int(tmp[1])

        if func == "add":
            s.add(val)
        elif func == "remove":
            s.discard(val)
        elif func == "check":
            print(1 if val in s else 0)
        elif func == "toggle":
            if val in s:
                s.discard(val)
            else:
                s.add(val)


