import sys

input = sys.stdin.readline

zeros = [1, 0]
ones = [0, 1]
for i in range(2, 41):
    zeros.append(zeros[i - 2] + zeros[i - 1])
    ones.append(ones[i - 2] + ones[i - 1])

t = int(input())
for _ in range(t):
    tmp = int(input())
    print(zeros[tmp], end=" ")
    print(ones[tmp])
