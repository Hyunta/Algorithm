import math


def calculate_min(time_in, time_out):
    in_h, in_m = map(int, time_in.split(":"))
    out_h, out_m = map(int, time_out.split(":"))
    tot = 0
    tot += (out_h - in_h) * 60
    tot += out_m - in_m
    return tot


def calculate_fee(fees, pmin):
    min_time, min_fee, unit_time, unit_fee = fees
    if pmin < min_time:
        return min_fee
    else:
        tot = min_fee
        pmin -= min_time
        tot += math.ceil(pmin / unit_time) * unit_fee
        return tot


def solution(fees, records):
    tot_time = {}
    curr_parking_lot = {}
    for record in records:
        ti, car_num, det = record.split(" ")
        if det == "IN":
            curr_parking_lot[car_num] = ti
        else:
            in_time = curr_parking_lot.pop(car_num)
            tot_time[car_num] = tot_time.get(car_num, 0) + calculate_min(in_time, ti)
    for car_num, in_time in curr_parking_lot.items():
        tot_time[car_num] = tot_time.get(car_num, 0) + calculate_min(in_time, "23:59")

    result = []
    for x in sorted(tot_time.keys()):
        result.append(calculate_fee(fees, tot_time[x]))

    return result


fl = [[180, 5000, 10, 600], ]
rl = [["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN",
       "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]]
expect = [[14600, 34400, 5000]]

for i in range(len(fl)):
    print(solution(fl[i], rl[i]))
    print(expect[i])
    print("-" * 50)
