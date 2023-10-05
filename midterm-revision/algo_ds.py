# # list
# x = [i for i in range(3)]
# print(x)

# # append, returns nothing
# print(x.append(1000))
# print(x)

# # insert, returns nothing 
# x.insert(2, 999)
# print(x.insert(2, 999))

# # remove, returns nothing 
# print(x.remove(2)) 
# print(x)

# # pop, returns the element at index that was popped
# print(x.pop(-3))
# print(x)
# print(x.pop()) # default = -1
# print(x)

# # prepend = insert = 0

# # repeat
# x = x * 2
# print(x)

# # tuple 
# # cant add anything
# # concatenation results in new tuple 
# x = (1,2,3)
# # print(x + (4)) # wont work, need ','
# y = x + ('element',) # , required
# print(y)

# print(2 in y)

# sets 
# x = {1,2,3.0, "ello"}
# print(x)
# x.add("1,2")
# print(x)
# cant add list to set 
# can add tuple to set  
# only add immutable element to set
# x.remove(3.0)



# with open('people.txt') as f: 
#     for line in f: 
#         print(line)
# or
# f = open('file.txt')

# always close 
# f.close()

from dataclasses import dataclass # VERY IMPORTANT NEED TO IMPORT 

@dataclass
class People: 
    name: str
    num1: str
    num2: str

p = []
with open('people.txt') as pfile: 
    line = pfile.readlines()[1:]
    for l in line:
        l = l.replace("\n", '')
        l = l.split(',')
        # print(l)
        p.append(People(l[0], l[1], l[2]))

print(p)