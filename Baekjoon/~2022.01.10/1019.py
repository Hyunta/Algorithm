import sys

n = int(sys.stdin.readline().replace("\n", ""))

counts = [0] * 10

weight = 1
for step in range(len(str(n))):
    replaced = int(str(n // 10) + "9")
    remaining = replaced - n
    for i in range(len(counts)):
        counts[i] += (n // 10 + 1) * weight
    for i in range(10 - remaining, 10):
        counts[i] -= weight
    for number in list(str(n)[:-1]):
        number = int(number)
        counts[number] -= remaining * weight

    counts[0] -= weight

    n //= 10
    weight *= 10

print(' '.join(map(str, counts)))
