# You are given an m x n integer grid accounts where accounts[i][j] 
# is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. 
# Return the wealth that the richest customer has.

def maxWealth(accounts):
    wealth = 0
    
    for i in accounts:
        if sum(i) > wealth:
            wealth = sum(i)
            
    return wealth

accounts = [[1,2,3],[3,2,1]]

print(maxWealth(accounts))