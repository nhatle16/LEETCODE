# https://leetcode.com/problems/add-binary/description/

def addBinary(a: str, b: str) -> str:
    ans = ""
    carry = False  # create a carry for binary addition
    longer = a if len(a) > len(b) else b
    shorter = b if len(b) < len(a) else a
    
    for i in range(len(longer)-len(shorter)):
        shorter = '0' + shorter

    for i in range(len(shorter)-1, -1, -1):     # iterate in a descending order
        value = int(shorter[i]) + int(longer[i])    # calculate the sum
        if carry:   # add 1 if there is a carry
            value += 1
        if value == 3:
            value = 1
            carry = True
        elif value == 2:
            value = 0
            carry = True
        else:
            carry = False

        ans += str(value)
    if carry:
        ans += '1'
        
    return ans[::-1]
    
if __name__ == "__main__":
    a = input("Enter first binary string: ")
    b = input("Enter second binary string: ")
    
    res = addBinary(a, b)
    print(res)