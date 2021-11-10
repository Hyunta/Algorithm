import sys

input = sys.stdin.readline

lim = 246912
primes = [0, 0] + [1] * (lim - 1)
for i in range(2, int(lim ** 0.5) + 1):
    if primes[i]:
        for j in range(i + i, lim + 1, i):
            primes[j] = 0

while True:
    n = int(input())
    if n == 0:
        break
    cnt = 0
    print(sum(primes[n + 1: 2 * n + 1]))
