
courses = ['History', 'Math', 'Physics', 'CompSci']
courses_2 = ['Art', 'Education']
nums = [1, 5, 2, 4, 3]

# courses.insert(0, courses_2)  # will add list as an element
# courses.append(courses_2)     # will add list as an element
# courses.extend(courses_2)     # will add elements to the list

# courses.remove('Math')        # removes an element
# courses.pop()                 # returns the value it removed
# courses.reverse()             # reverses list
# courses.sort(reverse=True)    # sorts alphabetically (reverse reverses this order)
# nums.sort()                   # sorts in ascending order
# sortedCourses = sorted(courses)   # returns a sorted version of the list (w/o changing list)

print(courses)
print(courses[0])
print(courses.index('Math'))
print('Math' in courses)      # True

for item in courses:
    print(item)

for index, course in enumerate(courses, start=1):   # start=1 if you want to start the list at 1
    print(index, course)

course_str = ', '.join(courses)
print(course_str)
new_list = course_str.split(', ')
print(new_list)
