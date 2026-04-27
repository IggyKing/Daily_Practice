nums = [2,7,11,15]
target = 9

def two_sum(nums,target):
    d = {}
    for i in range(len(nums)):
        x = nums[i]
        if target - x in d:
            return [d[target - x],i]
        else:
            d[x] = i

    return []

print(two_sum(nums,target))

#自己写
nums = [2,7,11,15]
target = 9

def two_sum(nums,target):
    d = {}
    for i in range(len(nums)):
        x = nums[i]
        if target - x in d:
            return [d[target-x],i]
        else:
            d[x] = i

    return []

print(two_sum(nums,target))

