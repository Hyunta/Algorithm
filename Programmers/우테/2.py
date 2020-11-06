def solution(log):
    study_time = 0
    for i in range(0, len(log), 2):
        tot = 0
        s_h, s_m = log[i].split(':')
        e_h, e_m = log[i + 1].split(':')
        tot += (int(e_h) - int(s_h)) * 60 + (int(e_m) - int(s_m))
        if tot < 5:
            tot = 0
        if tot > 105:
            tot = 105
        study_time += tot
    study_hour = str(study_time // 60)
    study_min = str(study_time % 60)
    if len(study_hour) == 1:
        study_hour = '0' + study_hour
    if len(study_min) == 1:
        study_min = '0' + study_min
    return study_hour + ":" + study_min


print(solution(["08:30", "09:00", "14:00", "16:00", "16:01", "16:06", "16:07", "16:11"]))
print(solution(["01:00", "08:00", "15:00", "15:04", "23:00", "23:59"]))
