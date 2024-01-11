def sumIndicesWithKSetBits(nums, k):
    sum = 0
    
    for i in range(len(nums)):
        bi_num = bin(i).replace("0b","")
        
        if bi_num.count('1') == k:
            sum += nums[i]
            
    return sum

nums = [5,10,1,5,2]
k = 1

print(sumIndicesWithKSetBits(nums, k))