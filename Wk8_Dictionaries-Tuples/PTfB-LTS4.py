# can't change tuples because they're immutable
# Mutable:
list1 = ['History', 'Math', 'Physics', 'CompSci']
list2 = list1

print(list1)
print(list2)

list1[0] = 'Art'
print(list1)
print(list2)

# Immutable:
tuple1 = ('History', 'Math', 'Physics', 'CompSci')
tuple2 = tuple1

print(tuple1)
print(tuple2)

tuple1[0] = 'Art'       # Error: tuple does not support item assignment
print(tuple1)
print(tuple2)
