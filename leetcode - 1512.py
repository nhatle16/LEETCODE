def numIdenticalPairs(nums):
    return len([(i, j) for i in range(len(nums)) for j in range(i+1, len(nums)) if nums[i] == nums[j]])

nums = [1,1,1,1]

print(numIdenticalPairs(nums))