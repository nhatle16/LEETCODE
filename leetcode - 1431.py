# There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number
# of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

# Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies

def kidsWithCandies(candies, extraCandies):
    return [True if (candies[i] + extraCandies >= max(candies)) else False for i in range(len(candies))]

def kidsWithCandies2(candies, extraCandies):
    ans = []
    most = max(candies)
    for i in candies:
        if i + extraCandies >= most:
            ans.append(True)
        else:
            ans.append(False)
            
    return ans

candies = [2,3,5,1,3]
extra = 3

print(kidsWithCandies2(candies, extra))