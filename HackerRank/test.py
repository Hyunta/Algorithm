rate = 1.10
origin = 100000000

print(f"초기 비용 : {origin:,}원")
for i in range(70):
    origin *= rate
    if i % 5 == 4:
        print(f"{i + 1}년후 : {int(origin):,}원")
print(origin)

in_money = 10000000
total = 70000000
for i in range(70):
    total *= rate
    total += in_money
    if i % 5 == 4:
        print(f"{i + 1}년후 : {int(total):,}원")
