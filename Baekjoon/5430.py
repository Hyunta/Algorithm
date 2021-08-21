import sys
input = lambda : sys.stdin.readline().strip()

t = int(input())
for _ in range(t):
    p = input()
    n = int(input())
    de = input()[1:-1].split(',')
    p = p.replace("RR","")

    direction = 0
    front, back = 0, 0
    for x in p:
        if x == "R":
            direction += 1
        elif x == "D":
            if direction % 2 == 0:
                front += 1
            else:
                back += 1
    if front + back <= n:
        de = de[front:n-back]

        if direction % 2 == 1:
            print('['+','.join(de[::-1])+']')
        else:
            print("[" + ",".join(de) + "]")
    else:
        print("error")