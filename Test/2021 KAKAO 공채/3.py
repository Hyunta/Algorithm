import math


def solution(fees, records):
    park = {}
    tot_time = {}
    for record in records:
        split = record.split()
        car_number = split[1]
        if car_number in park.keys():
            inh, inm = map(int, park[car_number].split(":"))
            outh, outm = map(int, split[0].split(":"))
            time_stamp = calculate_time(inh, inm, outh, outm)
            tot_time[car_number] = tot_time.get(car_number, 0) + time_stamp
            del park[car_number]
        else:
            park[car_number] = split[0]
    if park.keys():
        for key,value in park.items():
            inh,inm = map(int,value.split(":"))
            outh,outm = 23,59
            time_stamp = calculate_time(inh, inm, outh, outm)
            tot_time[key] = tot_time.get(key,0) + time_stamp

    result = []
    for number,time in tot_time.items():
        if time <= fees[0]:
            result.append([number,fees[1]])
        else:
            tmp = math.ceil((time - fees[0])/fees[2])
            tmp *= fees[3]
            tmp += fees[1]
            result.append([number,tmp])
    result.sort(key=lambda x:x[0])
    answer =[]
    for x in result:
        answer.append(x[1])
    return answer



def calculate_time(inh, inm, outh, outm):
    if inh == outh:
        tmp = outm - inm
    else:
        tmp = (outh - inh) * 60
        tmp += outm - inm
    return tmp


print(solution([180, 5000, 10, 600],
               ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN",
                "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
print(solution([120, 0, 60, 591],
               ["16:00 3961 IN", "16:00 0202 IN", "18:00 3961 OUT", "18:00 0202 OUT", "23:58 3961 IN"]))
print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))
