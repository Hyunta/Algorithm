import sys
input = sys.stdin.readline
leftBound, rightBound = map(int, input().split())
primes = [False for _ in range(rightBound-leftBound + 2)]
cnt = rightBound - leftBound + 1
i = 2
while i**2 <= rightBound:
    tmp = leftBound // (i ** 2)
    if leftBound % (i**2) != 0:
        tmp += 1

    while tmp*(i**2) <= rightBound:
        if not primes[tmp*(i**2) - leftBound]:
            primes[tmp*(i**2) - leftBound] = True
            cnt -= 1
        tmp += 1
    i += 1
print(cnt)

