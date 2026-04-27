#任务1：自己写冒泡排序
arr = [5,2,8,1,9]
n = len(arr)

for i in range(n):
    for j in range(n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j],arr[j + 1] = arr[j + 1],arr[j]

print(arr)

#任务2：降序排序
arr = [5,2,8,1,9]
n = len(arr)

for i in range(n):
    for j in range(n - i - 1):
        if arr[j + 1] > arr[j]:   #arr[j] < arr[j + 1]
            arr[j],arr[j + 1] = arr[j + 1],arr[j]

print(arr)

#任务3：第二大值
arr = [5,2,8,1,9]

max1 = arr[0]
max2 = arr[0]

for x in arr:
    if x > max1:
        max2 = max1
        max1 = x
    elif x > max2 and x != max1:
        max2 = x

print(max2)
