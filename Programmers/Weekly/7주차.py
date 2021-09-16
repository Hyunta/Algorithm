def solution(enter, leave):
    room = []
    met = [0] * len(enter)
    tmp = 0
    for l in leave:
        while l not in room:
            room.append(enter[tmp])
            tmp += 1
        room.remove(l)
        for p in room:
            met[p - 1] += 1
        met[l - 1] += len(room)
    return met


print(solution([1, 3, 2], [1, 2, 3]))
print("-----------")
print(solution([1, 4, 2, 3], [2, 1, 3, 4]))
