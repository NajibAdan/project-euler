def collatz_chain(x):
    if x == 1:
        return 1
    elif x in sample:
        return sample[x]
    elif x%2 == 0:
        y = x/2
    else:
        y = 3*x + 1
    return 1 + collatz_chain(y)

sample = {}
for x in range(1,1_000_000):
    if x not in sample:
        sample[x] = collatz_chain(x)

print(max(range(1,1_000_000),key=collatz_chain))
for x,y in sample.items():
    if y == max(sample.values()):
        print(x)