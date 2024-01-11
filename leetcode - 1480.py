def runningSum(nums):
    val = 0
    ans = []
    for i in nums:
        val += i
        ans.append(val)
        
    return ans

nums = [1,1,1,1,1]
print(runningSum(nums))