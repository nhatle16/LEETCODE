def countKDiff(nums, k):
    i, j = 0, 1
    count = 0
    
    while i < len(nums) and j < len(nums):
        if abs(nums[i] - nums[j]) == k:
            count += 1
        
        j += 1
        if j == len(nums):
            i += 1
            j = i+1
            
    return count

nums = [1,2,2,1]
k = 1

print(countKDiff(nums, k))