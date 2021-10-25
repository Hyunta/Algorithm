a = int(input())
operations = []
for _ in range(a):
    operations.append(input())

result = [1]
tmp = []
cur = 1
for op in operations:
    if op == "branch":
        if tmp:
            result.append(tmp.pop(0))
        else:
            cur += 1
            result.append(cur)
    else:
        a, b = op.split()
        b = int(b)
        print(b)
        tmp.append(result.remove(b))

print(result)
