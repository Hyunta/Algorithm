def solution(numbers):
    tmp = [i for i in range(1,10)]
    for number in numbers:
        while number in tmp:
            tmp.remove(number)
    return sum(tmp)

print(solution([1,2,3,4,6,7,8,0]))