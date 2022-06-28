# 8.13 List arguments

# def delete_head(t):
#     del t[0]
#
# letters = ['a', 'b', 'c']
# delete_head(letters)
# print(letters)
# # the parameter 't' and the variable 'letters' are alieases for the same object

t1 = [1, 2]
t2 = t1.append(3)
print(t1)
print(t2)

t3 = t1 + [3]
print(t3)
print(t2 is t3)
