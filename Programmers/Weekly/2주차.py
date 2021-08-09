def rate(avg:int)->str:
    if avg >= 90:
        return "A"
    elif 90 > avg >= 80:
        return "B"
    elif 80 > avg >= 70:
        return "C"
    elif 70 > avg >= 50:
        return "D"
    elif 50 > avg:
        return "F"

def solution(scores):
    answer = ""
    std = list(map(list, zip(*scores)))
    for i in range(len(std)):
        score = std[i]
        myScore = score[i]
        if (myScore == max(score) or myScore == min(score)) and score.count(myScore) == 1:
            score.remove(myScore)
        avg = sum(score) / len(score)
        answer += rate(avg)
    return answer

print(solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]))
print(solution([[50,90],[50,87]]))
print(solution([[70,49,90],[68,50,38],[73,31,100]]))