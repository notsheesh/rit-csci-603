# a = 97
# A = 65

# priority: not, and or 

# if __name__ == '__main__':

str = "hello"
print(str[2])
print(list(str))
print(''.join(list(str)))

'''
str.index(element) returns the index of element, value error if DNE. 
Think of it this way when you ask for index of something you assume its there 
And if its not you will get value error

str.find(element) returns -1 if DNE or index 
Now here the element doesn't have to be there, you are only asking python to find it 
'''

print(str.find("o"))
print(str.find("z"))
print(str.index("o"))
# print(str.index("z")) # Throws error


'''
Strip will remove space on either sides
'''
x = "      hello world"
print(x)
print(x.strip())
print(x.split())
