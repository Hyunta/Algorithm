def solution(weights, head2head):
    result = []
    for i in range(len(head2head)):
        lose = 0
        win = 0
        wei = 0
        for j in range(len(head2head[i])):
            if head2head[i][j] == "W":
                win += 1
                if weights[i] < weights[j]:
                    wei += 1
            elif head2head[i][j] == "L":
                lose += 1
        if win + lose == 0:
            rate = 0
        else:
            rate = win / (win + lose)
        result.append([rate, wei, weights[i], i + 1])
    result.sort(key=lambda x: (x[0], x[1], x[2], -x[3]), reverse=True)
    answer = []
    for x in result:
        answer.append(x[3])
    return answer


print(solution([50, 82, 75, 120], ["NLWL", "WNLL", "LWNW", "WWLN"]))
