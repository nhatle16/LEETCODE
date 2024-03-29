# https://leetcode.com/problems/plus-one/submissions/1205613645/

def PlusOne(digits: list) -> list:
    one: int = 1    # create a carry
    i: int = len(digits)-1    # index in the list
    
    while i >= 0:
        current = digits[i] + one
        digits[i] = current % 10
        one = current // 10
        
        if one == 0:
            break
        
        i -= 1
    
    if one == 1:
        digits.insert(0, one)
        
    return digits

def PlusOne2(digits: list) -> list:
    one: bool = True # create a carry
    i: int = 0      # index in the list
    digits = digits[::-1]
    
    while one:  # while the carry still exists
        if i < len(digits):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                one = False
                
            i += 1

        else:
            digits.append(1)
            one = False
        
    return digits[::-1]

if __name__ == "__main__":
    numbers = input("Enter a number: ")
    digits = [int(x) for x in numbers]
    result = PlusOne2(digits.copy())
    print("Plus one to {}, received {}".format(digits, result))