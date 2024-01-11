def leftRightDiff(nums):
    left, right = [0], [0]

    for i in range(len(nums)-1):
        left.append(left[i] + nums[i])

    val = 0
    for i in range(len(nums)-1, 0, -1):
        val += nums[i]
        right = [val] + right
        
    ans = [abs(left[i] - right[i]) for i in range(len(left))]
    
    return ans

def leftRightDiff2(nums):
    left = 0
    right = sum(nums)
    ans = []
    
    for i in range(len(nums)):
        right -= nums[i]
        ans.append(abs(right-left))
        left += nums[i]
        
    return ans


lis = [10,4,8,3]
print(leftRightDiff(lis))
print(leftRightDiff2(lis))