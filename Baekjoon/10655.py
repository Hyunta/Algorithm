import sys

input = sys.stdin.readline
n = int(input())
check_points = []
for _ in range(n):
    check_points.append(list(map(int, input().split())))

maxDiff = 0
for i in range(1, n - 1):
    diff = (abs(check_points[i + 1][0] - check_points[i][0]) + abs(check_points[i + 1][1] - check_points[i][1]) + abs(
        check_points[i][0] - check_points[i - 1][0]) + abs(check_points[i][1] - check_points[i - 1][1])) - (
                   abs(check_points[i + 1][0] - check_points[i - 1][0]) + abs(
               check_points[i + 1][1] - check_points[i - 1][1]))
    maxDiff = max(diff, maxDiff)

x_axis = check_points[0][0]
y_axis = check_points[0][1]
totalValue = 0
for i in range(1, n):
    totalValue += (abs(check_points[i][0] - x_axis) + abs(check_points[i][1] - y_axis))
    x_axis = check_points[i][0]
    y_axis = check_points[i][1]
print(totalValue - maxDiff)
