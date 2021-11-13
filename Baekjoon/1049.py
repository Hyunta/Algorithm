import sys

input = sys.stdin.readline

n, m = map(int, input().split())
package_price = 1001
one_price = 1001
for _ in range(m):
    pp, op = map(int, input().split())
    package_price = min(package_price, pp)
    one_price = min(one_price, op)

if (one_price * (n % 6)) > package_price:
    price = package_price * (n // 6 + 1)
elif package_price > one_price * 6:
    price = one_price * n
else:
    price = package_price * (n // 6) + one_price * (n % 6)
print(price)
