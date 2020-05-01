# Enumerate function, we use with for loop

# item in iterable

# without enumerate

name = ["abc", "abcde", "Anoop"]
pos = 0
for nam in name:
    print(f"{pos}------->{nam}")
    pos +=1


## with enumerate
for pos1, nam1 in enumerate(name):
    print(f"{pos1}------->{nam1}")

## with enumerate

def find_pos(l, target):

    for pos2, nam2 in enumerate(l):
        if nam2 == target:
            return pos2
    return -1
print(find_pos(name, "Anoop"))




















