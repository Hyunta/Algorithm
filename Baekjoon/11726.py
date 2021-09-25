import sys
input = sys.stdin.readline

n = int(input())
solution = [0,1,2]
for i in range(3,1001):
    solution.append(solution[i-2] + solution[i-1])
print(solution[n] % 10007)

