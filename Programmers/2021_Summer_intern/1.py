def solution(t, r):
    li = list()
    res = list()
    for i in range(len(t)):
        li.append([t[i],r[i],i])
    li.sort(key=lambda x: (x[0],x[1]))
    print(li)
    while li:
        tmp = li.pop(0)
        res.append(tmp[2])
        time = tmp[0]
        for x in li:
            if x[0] == time:
                x[0] += 1
        li.sort(key=lambda x: (x[0],x[1]))
    return res
