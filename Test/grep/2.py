from collections import OrderedDict
def solution(grades):
    score_dic = {"A+":1,"A0":2,"A-":3,"B+":4,"B0":5,"B-":6,"C+":7,"C0":8,"C-":9,"D+":10,"D0":11,"D-":12,"F":13}
    result = OrderedDict()
    seq = list()
    for grade in grades:
        grade = list(map(str, grade.split()))
        num = grade[0]
        score = grade[1]
        seq.append(grade[0])

        if num not in result.keys():
            result[num] = score

        if num in result.keys():
            tmp = result[num]
            if score_dic[score] < score_dic[tmp]:
                result[num] = score
                seq.pop(seq.index(num))
    tmp_answer = list(sorted(result.items(), key=lambda x: [score_dic[x[1]],seq.index(x[0])]))
    answer = []
    for x in tmp_answer:
        answer.append(x[0] +" "+ x[1])
    return answer





print(solution(["DS7651 A0", "CA0055 D+", "AI5543 C0", "OS1808 B-", "DS7651 B+", "AI0001 F", "DB0001 B-", "AI5543 D+", "DS7651 A+", "OS1808 B-"]))
print(solution(["DM0106 D-", "PL6677 B+", "DM0106 B+", "DM0106 B+", "PL6677 C0", "GP0000 A0"]))