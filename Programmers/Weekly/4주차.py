def solution(table, languages, preference):
    res = 0
    answer = ""
    for info in table:
        info = list(map(str, info.split()))
        sum = 0
        for i in range(len(languages)):
            if languages[i] in info:
                sum += (6 - info.index(languages[i]))*preference[i]
        if sum > res:
            answer = info[0]
            res = sum
        elif sum == res and info[0][0] < answer[0]:
            answer = info[0]
    return answer



print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
                "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
                "GAME C++ C# JAVASCRIPT C JAVA"], ["PYTHON", "C++", "SQL"], [7, 5, 5]))
print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
                "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
                "GAME C++ C# JAVASCRIPT C JAVA"], ["JAVA", "JAVASCRIPT"], [7, 5]))
