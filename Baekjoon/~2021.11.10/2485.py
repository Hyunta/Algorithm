import sys

input = sys.stdin.readline

n = int(input())
trees = list(int(input()) for _ in range(n))
distances = []
for i in range(1, len(trees)):
    distances.append(trees[i] - trees[i - 1])


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


tmp = distances[0]
for d in distances:
    tmp = gcd(tmp, d)

length = ((trees[-1] - trees[0])// tmp) + 1
print(length - n)