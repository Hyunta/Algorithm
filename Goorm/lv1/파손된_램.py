import sys
input = sys.stdin.readline

n = int(input())
m_list = list(map(int, input().split()))
errors = []

for i in range(len(m_list)):
	m = m_list[i]
	while m != 0:
		if m == 2:
			break
		if m % 2 != 0:
			errors.append(i+1)
			break
		m = m //2

print(len(errors))
print(*errors)