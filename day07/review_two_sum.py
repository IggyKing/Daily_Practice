#暴力法
nums = [2,7,11,15]
target = 9

for i in range(len(nums)):
    for j in range(i + 1,len(nums)):
        if nums[i] + nums[j] == target:
            print(i,j)

#暴力法自己写
nums = [2,7,11,15]
target = 9

for i in range(len(nums)):
    for j in range(i + 1,len(nums)):
        if nums[i] + nums[j] == target:
            print(i,j)

#哈希表
nums = [2,7,11,15]
target = 9

def two_sum(nums,target):
    d = {}

    for i in range(len(nums)):
        x = nums[i]

        if target - x in d:
            return [d[target - x],i]

        d[x] = i

    return []

print(two_sum(nums,target))

#哈希表尝试
nums = [2,7,11,15]
target = 9

def two_sum(nums,target):
    d = {}

    for i in range(len(nums)):
        x = nums[i]

        if target - x in d:
            return [d[target - x],i]

        d[x] = i

    return []

print(two_sum(nums,target))

#哈希表自己写
nums = [2,7,11,15]
target = 9

def two_sum(nums,target):
    d = {}

    for i in range(len(nums)):
        x = nums[i]

        if target - x in d:
            return[d[target - x],i]

        d[x] = i

    return []

print(two_sum(nums,target))
