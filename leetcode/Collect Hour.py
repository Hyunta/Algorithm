'''
  Collect Hour
  1. 0-9로 이루어진 A,B,C,D 변수를 입력받고,
  2. 4개의 변수를 조합하여 00:00 ~ 23:59 사이의 가능한 숫자를 생성하여야 함.
  3. int A = 1, B = 8, C = 3, D = 2가 주어졌을때, 함수는 6 을 응답하여야 함.
    12:38, 13:28, 18:23, 18:32, 21:38 and 23:18
'''


def collect_hour(A, B, C, D):
    nums = [A, B, C, D]
    possible_nums = 0

    for i in range(4):
        for j in range(4):
            if i != j:
                for k in range(4):
                    for l in range(4):
                        if (nums[i] * 10 + nums[j]) < 24 and (nums[k] * 10 + nums[l]) < 60:
                            possible_nums += 1

    return possible_nums
