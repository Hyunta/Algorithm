import sys

input = sys.stdin.readline


def get_least_distance():
    if center_count >= sensor_count:
        return 0

    distance = []
    for i in range(1, sensor_count):
        distance.append(sensor_location[i] - sensor_location[i - 1])

    distance.sort()
    for _ in range(center_count - 1):
        distance.pop()
    return sum(distance)


sensor_count = int(input())
center_count = int(input())
sensor_location = list(map(int, input().split()))
sensor_location.sort()

answer = get_least_distance()
print(answer)
