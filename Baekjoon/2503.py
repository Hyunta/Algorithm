import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())
total = list(permutations([i for i in range(1, 10)], 3))

for _ in range(n):
    test, strike, ball = map(int, input().split())
    test = list(str(test))
    remove_cnt = 0

    for i in range(len(total)):
        s_cnt, b_cnt = 0, 0
        i -= remove_cnt

        for j in range(3):
            test[j] = int(test[j])
            if test[j] in total[i]:
                if test[j] == total[i][j]:
                    s_cnt += 1
                else:
                    b_cnt += 1

        if s_cnt != strike or b_cnt != ball:
            total.remove(total[i])
            remove_cnt += 1
print(len(total))



