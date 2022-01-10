import sys
from itertools import product

input = sys.stdin.readline

n, k = map(int, input().split())
numbers = list(map(str, input().split()))
size = len(str(n))

while True:
    tmp = list(product(numbers, repeat=size))
    answer = []

    for x in tmp:
        if int("".join(x)) <= n:
            answer.append(int("".join(x)))
    if len(answer) >= 1:
        print(max(answer))
        break
    else:
        size -= 1
