import sys

input = sys.stdin.readline
resistance = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
answer = ""
for _ in range(2):
    answer += str(resistance.index(input().rstrip()))
answer = int(answer) * (10 ** resistance.index(input().rstrip()))
print(answer)
