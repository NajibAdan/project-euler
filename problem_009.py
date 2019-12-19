# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2

# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# My soln
maximum = 1000

for x in range(1,maximum+1):
    for y in range(1,maximum+1):
        z = maximum - x -y
        if x ** 2 + y ** 2 == z ** 2:
            print(x,y,z,x*y*z)
            break
