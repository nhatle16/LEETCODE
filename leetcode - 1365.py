def smallerThanCur(nums):
    ans = []
    for i in nums:
        smaller = [i for j in nums if j < i]
        ans.append(len(smaller))
        
    return ans

nums = [8,1,2,2,3]
print(smallerThanCur(nums))