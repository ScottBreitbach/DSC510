
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#          0, 1, 2, 3, 4, 5, 6, 7, 8, 9     the positive indexes
#        -10,-9,-8,-7,-6,-5,-4,-3,-2,-1     the negative indexes

# list[start:end:step]

print(my_list[-7:10])
print(my_list[2:-1:2])
print(my_list[-1:2:-2])     # when using negative step, must work right to left
print(my_list[::-1])        # if you just want to reverse a list

t1 = my_list[5]
t2 = my_list[5:6]

print(t1, type(t1))
print(t2, type(t2))
