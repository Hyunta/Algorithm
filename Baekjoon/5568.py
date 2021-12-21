import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())
k = int(input())
cards = []
numbers = set()


for _ in range(n):
    cards.append((input().rstrip()))

pair_by_k = list(permutations(cards, k))
for pair in pair_by_k:
    tmp_number = "".join(pair)
    numbers.add(tmp_number)

print(len(numbers))
