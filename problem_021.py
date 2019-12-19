# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are 
# called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; 
# therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.
import math
def divisors(number):
    divisors_list = []
    for i in range(1,int(math.sqrt(number)+1)):
        if number % i == 0:
            yield i
            if i * i != number:
                divisors_list.append(number/i)
    for divisor in reversed(divisors_list):
        yield divisor

number = []
for i in range(1,10_000):
    x = int(sum(list(divisors(i))[:-1]))
    y = int(sum(list(divisors(x))[:-1]))
    if i == y and i!=x:
        if i not in number:
            number.append(i)
        if y not in number:
            number.append(y)

print(sum(number))