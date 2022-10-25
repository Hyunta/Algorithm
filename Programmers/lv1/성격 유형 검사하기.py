def solution(survey, choices):
    dict = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}

    for idx, val in enumerate(choices):
        if (val > 4):
            dict[survey[idx][1]] += val - 4
        else:
            dict[survey[idx][0]] += 4 - val

    answer = ""
    if dict['R'] < dict['T']:
        answer += 'T'
    else:
        answer += 'R'

    if dict['C'] < dict['F']:
        answer += 'F'
    else:
        answer += 'C'

    if dict['J'] < dict['M']:
        answer += 'M'
    else:
        answer += 'J'

    if dict['A'] < dict['N']:
        answer += 'N'
    else:
        answer += 'A'

    return answer

solution()
