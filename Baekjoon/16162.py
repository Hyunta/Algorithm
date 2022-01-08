import sys

input = sys.stdin.readline

n, a, d = map(int, input().split())
sound = list(map(int, input().split()))

tot = 0
current_sound = 0
for s in sound:
    if s == a and tot == 0:
        current_sound = s
        tot += 1
    elif current_sound != 0 and s == current_sound + d:
        current_sound = s
        tot += 1
print(tot)
