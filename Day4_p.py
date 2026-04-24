#（1）函数定义
arr = [5,2,8,1,9]
max_num = arr[0]

for x in arr:
    if x > max_num:
        max_num = x

print(max_num)

def find_max(arr):
    max_num = arr[0]

    for x in arr:
        if x in arr:
            if x > max_num:
                max_num = x

    return max_num

arr = [5,2,8,1,9]
print(find_max(arr))

#（2）函数结构
def 函数名(参数):
    代码
    return 返回值

#（3）简单举例
def add(a,b):
    return a + b

print(add(3,5))

#（4）return是什么
# return 值    意思是：把结果交出去

# 没有return会怎样？
def test():
    print("hello")

print(test())
#输出：
#hello
#None
#因为函数没有返回值
