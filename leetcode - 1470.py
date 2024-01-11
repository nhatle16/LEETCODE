def shuffleList(nums):
    n = int(len(nums) / 2)
    ans = []
    
    for i in range(n):
        ans.append(nums[i])
        ans.append(nums[i+n])
        
    return ans

lis = [2,5,1,3,4,7]

print(shuffleList(lis))