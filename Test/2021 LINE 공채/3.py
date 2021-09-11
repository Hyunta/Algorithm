from collections import deque


def solution(jobs):
    init = jobs.pop(0)
    time = init[0] + init[1]
    order = [init[2]]
    task = []
    while time < 50:
        imp = [0]*100
        for i in range(len(jobs)):
            print(jobs[i][0], time)
            if jobs[i][0] <= time:
                task.append(jobs[i])
            else:
                jobs = jobs[i:]
                break

        for i in range(len(task)):
            if task[i][2] == order[-1]:
                break
            imp[task[i][2]] += task[i][3]
        else:
            for j in range(100):
                if imp[j] == max(imp):
                    for k in range(len(task)):
                        if task[k] == j:
                            i = k
                            break
            # 분류번호 같은게 없는 경우
        tmp = task.pop(i)
        time += tmp[1]
        if order[-1] != tmp[2]:
            order.append(tmp[2])



print(solution([[1, 5, 2, 3], [2, 2, 3, 2], [3, 1, 3, 3], [5, 2, 1, 5], [7, 1, 1, 1], [9, 1, 1, 1], [10, 2, 2, 9]]))
# print(solution([[1, 2, 1, 5], [2, 1, 2, 100], [3, 2, 1, 5], [5, 2, 1, 5]]))
# print(solution([[0, 2, 3, 1], [5, 3, 3, 1], [10, 2, 4, 1]]))
# print(solution([[0, 5, 1, 1], [2, 4, 3, 3], [3, 4, 4, 5], [5, 2, 3, 2]]))