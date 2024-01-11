def countPairs(nums, target):
    return len([(i, j) for i in range(len(nums)) for j in range(i + 1, len(nums)) if (nums[i] + nums[j]) < target])


nums = [-6,2,5,-2,-7,-1,3]
target = -2

print(countPairs(nums, target))