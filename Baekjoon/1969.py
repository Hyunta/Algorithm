import sys

input = sys.stdin.readline

n, m = map(int, input().split())
dna = [input().rstrip() for _ in range(n)]

dna_to_num = {"A": 0, "C": 1, "G": 2, "T": 3}
num_to_dna = {0: "A", 1: "C", 2: "G", 3: "T"}

res = ""
cnt = 0

for i in range(m):
    check = [0] * 4
    for j in range(n):
        check[dna_to_num[dna[j][i]]] += 1

    max_dna = max(check)
    max_dna_idx = check.index(max_dna)
    res += num_to_dna[max_dna_idx]
    check[max_dna_idx] = 0
    cnt += sum(check)

print(res)
print(cnt)