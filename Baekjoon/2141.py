import sys
input = sys.stdin.readline

village_count = int(input())
total_people = 0
village_info = []
for _ in range(village_count):
    tmp_village = list(map(int, input().split()))
    village_info.append(tmp_village)
    total_people += tmp_village[1]

village_info.sort(key=lambda x: [x[0], x[1]])

mid = total_people // 2
if total_people % 2 == 1:
    mid += 1

count = 0
for location, people in village_info:
    count += people

    if count >= mid:
        print(location)
        break
