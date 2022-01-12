import sys

input = sys.stdin.readline
n = int(input())
target_heights = list(map(int, input().split()))
watering_count = sum(target_heights) // 3

if sum(target_heights) % 3 != 0:
    print("NO")
else:
    for height in target_heights:
        watering_count -= height // 2
    if watering_count > 0:
        print("NO")
    else:
        print("YES")
