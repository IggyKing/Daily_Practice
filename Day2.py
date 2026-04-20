#任务1：找最大值
arr = [5,2,8,1,9]
max_num = 0;
for i in range(5):
    if max_num < arr[i]:
        max_num = arr[i]
print(max_num)

#任务1修正(1)：数组内容可能为负 应该以第一个元素当初始最大值
arr = [5,2,8,1,9]
max_num = arr[0]
for i in range(len(arr)):
    if arr[i] > max_num:
        max_num = arr[i]
print(max_num)

#任务1修正(2)：更python 不用i 直接拿元素
arr = [5,2,8,1,9]
max_num = arr[0]
for x in arr:
    if x > max_num:
        max_num = x
print(max_num)

#任务2：求数组总和
arr = [5,2,8,1,9]
total = 0
for x in arr:
    total += x
print(total)

#任务2pro：求数组中偶数的和
arr = [5,2,8,9,1]
total = 0
for x in arr:
    if(x%2==0):   #if x % 2 == 0:
        total += x
print(total)

#任务2promax：求数组中最大的偶数
arr = [5,2,8,9,1]
for x in arr:
    if x % 2 == 0:
        max_num_ou = x
        if x > max_num_ou:
            max_num_ou = x
print(max_num_ou)

#任务2promax修正！
arr = [5,2,8,9,1]
max_num_ou = None   # 关键！
for x in arr:
    if x % 2 == 0:
        if max_num_ou is None or x > max_num_ou:
            max_num_ou = x
print(max_num_ou)

#任务2promax自己写
arr = [5,2,8,9,1]
max_num_ou = None
for x in arr:
    if x % 2 == 0:
        if max_num_ou == None or x > max_num_ou:
            max_num_ou = x
print(max_num_ou)

#任务3：反转数组（不用reserve）
arr = [5,2,8,9,1]

n = len(arr)

for i in range(n//2):
    arr[i],arr[n - i - 1] =arr[n - i - 1],arr[i]

print(arr)
