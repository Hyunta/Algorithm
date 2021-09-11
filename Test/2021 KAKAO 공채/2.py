def convert(number, base):
    T = "0123456789"
    q, r = divmod(number, base)
    return convert(q, base) + T[r] if q else T[r]


def prime_list(n):
    check = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if check[i] == True:
            for j in range(i + i, n, i):
                check[j] = False
    return [i for i in range(2, n) if check[i] == True]


def isPrime(n,primes):
    for prime in primes:
        if prime >= n:
            break
        elif n % prime == 0:
            return False
    return True


def solution(n, k):
    number = convert(n, k)
    primes = prime_list(2000000)
    split = number.split("0")
    cnt = 0
    for x in split:
        if x:
            if int(x) > 2000000:
                if isPrime(int(x),primes):
                    cnt += 1
            if int(x) in primes:
                cnt += 1
    return cnt


print(solution(437674, 3))
print(solution(110011, 10))
print(solution(0,10))
print(solution(987123456829,10))
