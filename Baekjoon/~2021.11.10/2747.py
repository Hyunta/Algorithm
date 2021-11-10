import sys

input = sys.stdin.readline

fiv = [0, 1, 1] + [0] * 43
for i in range(3, 46):
    fiv[i] = fiv[i - 1] + fiv[i - 2]
print(fiv[int(input())])
