import sys

input = sys.stdin.readline

val = input().rstrip()
stack = []
index = [-1 for _ in range(len(val))]
curr_num = 0

for idx, ch in enumerate(val):
    if ch == '(':
        index[idx] = curr_num
        stack.append(idx)
        curr_num += 1
    elif ch == ')':
        index[idx] = index[stack.pop()]

choose = [0 for _ in range(curr_num)]
answers = []


def find_answers(cnt):
    if cnt == curr_num:
        if sum(choose) == 0:
            return

        answer = ""
        for idx, ch in enumerate(val):
            if index[idx] == -1 or choose[index[idx]] == 0:
                answer += ch
        answers.append(answer)
        return

    choose[cnt] = 1
    find_answers(cnt + 1)
    choose[cnt] = 0
    find_answers(cnt + 1)


find_answers(0)
answers = sorted(set(answers))
print('\n'.join(answers))

