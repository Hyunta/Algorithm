def solution(student, k):
    cnt = 0
    for i in range(len(student)):
        for j in range(i, len(student)):
            tmp = student[i:j+1]
            print(tmp)
            if sum(tmp)==k:
                cnt += 1
    return cnt


print(solution([0, 1, 0, 0], 1))
print(solution([0, 1, 0, 0, 1, 1, 0], 2))
print(solution([0, 1, 0], 2))
