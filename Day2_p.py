#（1）列表
arr = [3,7,2,9,1]
print(arr)
print(arr[0])
print(arr[2])

#（2）遍历数组
for x in arr:
    print(x)

#（3）求最大值
arr = [3,7,2,9,1]
max_num = arr[0]
for x in arr:
    if x > max_num:
        max_num = x
print(max_num)

#（4）求数组和
arr = [3,7,2,9,1]
total = 0;
for x in arr:
    total += x
print(total)

#（5）反转数组
arr = [1,2,3,4,5]
n = len(arr)
for i in range(n//2):
    arr[i],arr[n - i - 1] = arr[n - i - 1],arr[i]
print(arr)
