import sys
from collections import defaultdict
from datetime import datetime

input = sys.stdin.readline


def convert_datetime(date, time):
    year, month, day = map(int, date.split("-"))
    hour, minu = map(int, time.split(":"))
    return datetime(year, month, day, hour, minu)


n, l, f = input().split()

n, f = int(n), int(f)
fare_day, fare_time = l.split("/")
fare_hour, fare_min = map(int, fare_time.split(":"))
fare_time = (int(fare_day) * 1440) + (fare_hour * 60) + fare_min

rent = defaultdict()
fee = defaultdict(int)

for _ in range(int(n)):
    date, time, item, member = input().split()
    key_data = item + " " + member
    value_data = convert_datetime(date, time)

    if member not in rent:
        rent[member] = {}

    if item in rent[member]:
        start_datetime = rent[member].pop(item)
        diff_datetime = value_data - start_datetime
        diff_min = (diff_datetime.days * 1440) + (diff_datetime.seconds // 60)
        if diff_min > fare_time:
            fee[member] = fee.get(member, 0) + (diff_min - fare_time) * f
    else:
        rent[member][item] = value_data

if fee.keys():
    for key in sorted(fee.keys()):
        print(key, end=" ")
        print(fee.get(key))
else:
    print(-1)
