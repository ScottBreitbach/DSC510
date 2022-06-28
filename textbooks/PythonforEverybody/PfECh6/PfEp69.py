# # prints letters in order
#
# fruit = 'banana'
# for char in fruit:
#     print(char)


# prints a string starting at the last letter

fruit = 'banana'
index = -1
while index >= -(len(fruit)):
    print(fruit[index])
    index -= 1

print(fruit[:])

# string methods: https://docs.python.org/3/library/stdtypes.html#string-methods
print(fruit.replace('a', 'i'))  # bahahahaha
print(fruit.strip('ab'))

