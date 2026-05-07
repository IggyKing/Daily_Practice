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
