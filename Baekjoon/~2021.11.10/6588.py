import sys
input = sys.stdin.readline

mil = 1000000
check = [False,False] + [True] * mil

for i in range(2, 1001):
    if check[i]:
        for j in range(i * 2, mil, i):
            check[j] = False

while True:
    n = int(input())
    if n == 0: break
    lt = 0
    rt = n
    for _ in range(mil):
        if check[lt] and check[rt]:
            print(f"{n} = {lt} + {rt}")
            break
        lt += 1
        rt -= 1
    else:
        print("Goldbach's conjecture is wrong.")
