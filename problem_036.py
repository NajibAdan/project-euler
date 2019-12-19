# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

# (Please note that the palindromic number, in either base, may not include leading zeros.)

def toBinary(x):
    return bin(x)[2:]

def isPalindrome(x):
    if x == x[::-1]:
        return True
    else:
        return False

top = []
for x in range(1,1_000_000):
    if isPalindrome(str(x)) and isPalindrome(toBinary(x)):
        top.append(x)

print(sum(top))
