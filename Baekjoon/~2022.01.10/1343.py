import sys
input = sys.stdin.readline

p = input()

p = p.replace("XXXX", "AAAA")
p = p.replace("XX", "BB")

if "X" in p:
    print(-1)
else:
    print(p)

