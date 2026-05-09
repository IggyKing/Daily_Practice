#只处理（）：
s = "()"

stack = []

for c in s:
    if c == "(":
        stack.append(c)

    else:
        if len(stack) == 0:
            print(False)
            break

        stack.pop()

if len(stack) == 0:
    print(True)
else:
    print(False)

#完整逻辑：
s = "()[]{}"

stack = []
valid = True #合不合法的标记 一开始默认这个括号字符串是合法的

for c in s:
    if c == "(" or c == "[" or c == "{":
        stack.append(c)
    else:
        if len(stack) == 0:
            valid = False
            break

        top = stack[-1]

        if c == ")" and top == "(":
            stack.pop()
        elif c == "]" and top == "[":
            stack.pop()
        elif c == "}" and top == "{":
            stack.pop()
        else:
            valid = False
            break

if len(stack) == 0 and valid:
    print(True)
else:
    print(False)