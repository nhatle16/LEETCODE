# Add 1 to an array of integer

def plusOne(digits):
    digits = digits[::-1]
    one, i = True, 0
    
    while one:
        if i < len(digits):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                one = False
                
        else:
            digits.append(1)
            one = False
            
        i += 1
        
    return digits[::-1]

# 2nd version without reversing the list

def plusOne2(digits):
    one = 1
    i = len(digits) - 1
    
    while i >= 0:
        cur = digits[i] + one
       
        digits[i] = cur % 10
        one = cur // 10
        
        if not one:
            break
    
        i -= 1
        
    if one:
        digits.insert(0, one)
        
    return digits

arr1 = [1,0,1,2]
arr2 = [9,9,9]

print(plusOne2(arr1))
print(plusOne2(arr2))