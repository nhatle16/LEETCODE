def sumOddLengthSubArr(arr):
    sum_all = 0
    
    for i in range(len(arr)):
        jump = 1
        
        while i + jump <= len(arr):
            temp = sum(arr[i:i+jump])
            sum_all += temp
            jump += 2
            
        return sum_all
    
lis = [1,4,2,5,3]

print(sumOddLengthSubArr(lis))