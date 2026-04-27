#任务1：写函数求最大值
arr = [5,2,8,1,9]

def find_max(arr):
    max_num = arr[0]

    for c in arr:
        if max_num < c:
            max_num = c
    return max_num

print(find_max(arr))

#任务1pro：写函数求最小值
arr = [5,2,8,1,9]

def find_min(arr):
    min_num = arr[0]
                           #更规范自然：
    for c in arr:          #for x in arr:
        if min_num > c:    #   if x < min_num:
            min_num = c    #        min_num = x
    return min_num         #return min_num

print(find_min(arr))

#任务1pro更安全写法：考虑是否有空数组
def find_min(arr):
    if len(arr) == 0:
        return None

    min_num = arr[0]

    for x in arr:
        if x < min_num:
            min_num = x

    return min_num

#任务2：写一个函数实现回文判断
def is_palindrome(s):
    if len(s) == 0:              #不合理 return True 或者 直接删掉
        return None

    flag = True

    n = len(s)

    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            flag = False          #return False
                                  #即使已经不是回文了，循环还会继续跑
    return flag                   #改完后一旦发现不相等，直接结束

s = "aba"
print(is_palindrome(s))

s = "abcde"
print(is_palindrome(s))

#任务2pro：忽略大小写 "Aba" → True
def is_palindrome(s):
    #flag = True

    n = len(s)

    s = s.lower()

    for i in range(n // 2):
        if s[i] != s[n - i -1]:
            return False  #如果不符合回文 直接在这里结束函数 返回False

    return True
    #return flag

s = "Aba"
print(is_palindrome(s))

s = "abCde"
print(is_palindrome(s))

#任务3：写函数实现1-n求和(写错啦！求1-n的和 不是求数组n的累加和）
#def sum_n(n):
#    sum = 0

#    for c in n:
#        sum += c

#    return sum

#n = [1,2,3]
#print(sum_n())

#任务3改正：
def sum_n(n):
    total = 0

    for i in range(1,n + 1):
        total += i

    return total

print(sum_n(5))

#任务3pro：求1-n中所有偶数的和
def sum_even(n):
    total = 0

    for i in range(1,n + 1):
        if i % 2 == 0:
            total += i

    return total

print(sum_even(10))

#任务3pro更高级写法：不用if 用步长 更高效更优雅
def sum_even(n):
    total = 0

    for i in range(2,n + 1,2):   #表示：2, 4, 6, 8, ... 直接跳着走，不用判断
        total += i

    return total

#任务3promax：求1-n中所有奇数和
def sum_odd(n):
    total = 0

    for i in range(1,n + 1,2):
        total += i

    return total

