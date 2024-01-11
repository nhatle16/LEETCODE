def differenceOfSum(nums):
    if max(nums) == 9:
        return 0

    ele_sum = sum(nums)
    digit_sum = 0

    for i in nums:
        while i > 0:
            digit_sum += i % 10
            i //= 10

    return ele_sum - digit_sum

nums = [1,15,6,3]

print(differenceOfSum(nums))