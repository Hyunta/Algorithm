import sys

input = sys.stdin.readline

t = int(input())
bd = 2000000
check = [False, False] + [True] * bd
primes = []
for i in range(2, bd + 1):
    if check[i]:
        primes.append(i)
        for j in range(i * 2, bd + 1, i):
            check[j] = False


def isPrime(num):
    if num > bd:
        for prime in primes:
            if prime >= num:
                break
            elif num % prime == 0:
                return False
        return True
    else:
        return check[num]


for _ in range(t):
    a, b = map(int, input().split())
    tmp = a + b

    if tmp < 4:
        print("NO")

    elif tmp % 2 == 0:
        print("YES")

    else:
        if isPrime(tmp-2):
            print("YES")
        else:
            print("NO")
