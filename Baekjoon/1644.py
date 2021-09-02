import sys

r = sys.stdin.readline


def find_prime_numbers(num):
    check = [False, False] + [True] * (num - 1)
    primes = []
    for i in range(2, num + 1):
        if check[i]:
            primes.append(i)
            for j in range(i * 2, num + 1, i):
                check[j] = False
    return primes


n = int(r())
primeNumbers = find_prime_numbers(n)

lt = 0
rt = lt +1
cnt = 0
while lt != len(primeNumbers):
    bound = sum(primeNumbers[lt:rt])
    if bound < n:
        if rt == len(primeNumbers):
            break
        rt += 1
    elif bound == n:
        cnt += 1
        lt += 1
        rt += 1
    elif bound > n:
        lt += 1

print(cnt)