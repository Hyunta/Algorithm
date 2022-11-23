import math
import sys
from itertools import permutations

MAX = 1000001
isPrime = [True] * MAX


def find_prime():
    isPrime[0] = False
    isPrime[1] = False
    isPrime[2] = True
    for i in range(int(math.sqrt(MAX)) + 1):
        if isPrime[i]:
            for j in range(i * i, MAX, i):
                isPrime[j] = False


def dd(target_num, k):
    if target_num < k: return target_num
    while True:
        if target_num % k != 0: return target_num
        target_num //= k


def cond1(n):
    for i in range(2, n // 2 + 1):
        if i != n - i and isPrime[i] and isPrime[n - i]:
            return True
    return False


def cond2(n, k):
    n = dd(n, k)
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0 and isPrime[i] and isPrime[n // i]:
            return True
    return False


input = sys.stdin.readline

find_prime()
K, M = map(int, input().split())
ans = 0
for num in permutations(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], K):
    if num[0] == '0': continue
    num = int(''.join(num))
    if cond1(num):
        if cond2(num, M):
            ans += 1

print(ans)
