import sys

input = sys.stdin.readline
burger = 2000
bev = 2000
for _ in range(3):
    burger = min(burger, int(input()))
for _ in range(2):
    bev = min(bev, int(input()))
print(burger+bev-50)