#(1)什么是栈？
#可以理解成:盘子堆 只能放最上面 也只能拿最上面
#后进先出LIFO：Last In First Out
#(2)如何实现栈？
#直接用列表！
stack = []
#入栈：
stack.append(1)
stack.append(2)
print(stack)
#出栈：
stack.pop()
print(stack)
