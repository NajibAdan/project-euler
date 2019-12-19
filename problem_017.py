test = {
    1 : 'one',
    2 : 'two',
    3 : 'three',
    4 : 'four',
    5 : 'five',
    6 : 'six',
    7 : 'seven',
    8 : 'eight',
    9 : 'nine',
    10 : 'ten',
    11 : 'eleven',
    12 : 'twelve',
    13 : 'thirteen',
    14 : 'fourteen',
    15 : 'fifteen',
    16 : 'sixteen',
    17 : 'seventeen',
    18 : 'eighteen',
    19 : 'nineteen',
    20 : 'twenty',
    30 : 'thirty',
    40 : 'forty',
    50 : 'fifty',
    60 : 'sixty',
    70 : 'seventy',
    80 : 'eighty',
    90 : 'ninety',
    100  : 'hundred',
    1000 : 'thousand',
}

def getLength(x):
    if x == 100:
        print(test[1],test[100])
        return len(test[1]) + len(test[100])
    elif x == 1000:
        print(test[1],test[1000])
        return len(test[1]) + len(test[1000])
    elif (x in test):
        print(test[x])
        return len(test[x])
    elif x > 20 and x < 100:
        print(test[(x-x%10)],end=' ')
        return len(test[(x-x%10)]) + getLength(x%10)
    else:
        if x % 100 == 0:
            print(test[(x-x%100)/100],test[100])
            return len(test[(x-x%100)/100]) + len(test[100])
        else:
            print(test[(x-x%100)/100],test[100],'and',end=' ')
            return len(test[(x-x%100)/100]) + len(test[100]) + len('and') + getLength(x%100)

print(getLength(1000))
print(sum([getLength(x) for x in range(1,1001)]))
        