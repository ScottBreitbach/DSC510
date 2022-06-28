'''sets are values that are unordered and have no duplicates'''
'''used to see if values are part of a set (membership test)
and to remove duplicate values'''

# Sets
csCourses = {'History', 'Math', 'Physics', 'CompSci', 'Math'}

print(csCourses)
print('Math' in csCourses)  # can do with Lists/Tuples, but sets are optimized for this

'''see what values they share or don't share with other sets'''

artCourses = {'History', 'Math', 'Art', 'Design'}

print(csCourses.intersection(artCourses))   # what's in both sets?
print(csCourses.difference(artCourses))     # what's in one but not the other?
print(csCourses.union(artCourses))          # print entire list of courses

