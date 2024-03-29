# https://leetcode.com/problems/roman-to-integer/description/

def romanToInt(s: str) -> int:
    glossary: dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
        'D': 500, 'M': 1000
        }
    res: int = 0
    prev: int = 0
    
    for c in s:
        value: int = glossary[c]
        if prev < value:
            res += value - 2*prev
        else:
            res += value
            
        prev = value
        
    return res

if __name__ == "__main__":
    roman_exp = input("Enter a Roman expression: ")
    result = romanToInt(roman_exp)
    
    print("Converting {} to integer, received: {}".format(roman_exp, result))