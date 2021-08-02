import sys
# a1b2b4 --> a1b6
# 문자열 압축하기

input = sys.stdin.readline
st = input().rstrip()

# 문자열 나누기
st_li = []
tmp = ''
for x in st:
    if x.isalpha():
        if tmp:
            st_li.append(tmp)
            tmp = ''
    tmp += x
st_li.append(tmp)

st_dic = dict()
for x in st_li:
    st_dic[x[0]] = st_dic.get(x[0], 0) + int(x[1:])
for x, y in st_dic.items():
    print(x, end='')
    print(y, end='')


