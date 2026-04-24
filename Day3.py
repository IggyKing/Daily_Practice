#任务1：字符串反转
s = "hello"

res = ""

for c in s:
    res = c + res

print(res)

#任务1pro：忽略空格的反转
s = "a b c"

res = ""

for c in s:
    if c != " ":
        res = c + res

print(res)

#任务1promax：只反转字母 保留空格位置
s = "a b c"

res = ""

for c in s:
    res = c + res

print(res)

#任务1promax正确解法：
s = "a b c"

letters = []   #创建空列表

# 1️⃣ 先把所有字母提取出来
for c in s:
    if c != " ":
        letters.append(c)
#letters = ['a','b','c']

# 2️⃣ 反转字母
letters = letters[::-1]
#letters = ['c','b','a']

# 3️⃣ 再按原位置放回
res = ""
index = 0 # 记录当前应该从 letters 里取第几个字母

for c in s:
    if c == " ":
        res += " "
    else:
        res += letters[index]
        index += 1

print(res)

#自己写
s = "a b c"

letters = []

for c in s:
    if c != " ":
        letters.append(c)

letters = letters[::-1]

res = ""
index = 0

for c in s:
    if c == " ":
        res += " "
    else:
        res += letters[index]
        index += 1
print(res)