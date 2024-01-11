# Decompress a run-length encoded list

def decompressRLE(nums):
    ans = []
    for i in range(0, len(nums)-1, 2):
        fre, val = nums[i], nums[i+1]
        ans.extend([val] * fre)

    return ans

print(decompressRLE([1,2,3,4]))
print(decompressRLE([1,1,2,3]))