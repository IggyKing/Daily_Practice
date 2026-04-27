#(1)字符串
s = "hello"
print(s)

s = "hello"

print(s[0])  # h
print(s[1])  # e

#(2)遍历字符串
s = "hello"

for c in s:
    print(c) # 一个一个字符取出来\

#(3)字符串反转
s = "hello"

res = ""

for c in s:
    res = c + res

print(res)

#(4)回文判断
s = "aba"

n = len(s)

flag = True

for i in range(n // 2):
    if s[i] != s[n - i - 1]:
        flag = False
        break

print(flag)

#(5)统计字符出现次数
s = "aabbbc"

d = {}

for c in s:
    if c in d:
        d[c] += 1
    else:
        d[c] = 1

print(d)
