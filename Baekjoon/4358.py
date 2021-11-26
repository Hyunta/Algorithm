import sys

input = sys.stdin.readline
trees = {}
tot = 0
while True:
    tree = input().rstrip()
    if not tree:
        break
    trees[tree] = trees.get(tree, 0) + 1
    tot += 1

names = list(trees.keys())
names.sort()
for name in names:
    print(f'{name} {(trees[name] / tot) * 100:.4f}')
