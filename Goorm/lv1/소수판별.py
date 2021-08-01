import sys

input = sys.stdin.readline

n = int(input())

isPrime = [False, False] + [True] * (n - 1)
primes = []
for i in range(2, n + 1):
    if isPrime[i]:
        primes.append(i)
        for j in range(i * 2, n + 1, i):
            isPrime[j] = False
print(isPrime[n])

