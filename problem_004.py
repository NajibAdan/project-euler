# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.
palindromes = []
for x in range(100,1000):
    for y in range(100,1000):
        if str(x*y) == str(x*y)[::-1]:
            palindromes.append(x*y)


print(max(palindromes))

