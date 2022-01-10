import sys

input = sys.stdin.readline
n = int(input())
drinks = list(map(int, input().split()))
drinks.sort()
last = drinks.pop()
last += sum(drinks) / 2
print(last)
