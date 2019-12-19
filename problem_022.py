f = open('problem_022.txt').readlines()
def char_position(letter):
    return ord(letter.lower()) - 96
names = ""
for x in f[0].replace('"',''):
    names += x
names_list = names.split(',')
names_list.sort()
count = 0
t = "COLIN"
print(names_list)
print(sum([char_position(x) for x in t])*(names_list.index(t)+1))
for x in names_list:
    count += sum([char_position(y) for y in x]) * (names_list.index(x)+1)
print(count)