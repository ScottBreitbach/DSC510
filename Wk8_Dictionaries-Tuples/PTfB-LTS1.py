'''Lists, Tuples, and Sets'''

courses = ['History', 'Math', 'Physics', 'CompSci']
courses2 = ['Music', 'English']
print(courses[0])
print(len(courses))

courses.append('PE')
courses.insert(0, 'Art')
# courses.insert(0, courses2)     # adds the entire list to one value in the list
courses.extend(courses2)        # adds the individual items to the list
courses.remove('Math')
# courses.pop()                 # will remove last item from list (and return it)
popped = courses.pop()          # sets to value that was popped
print(popped)
print(courses)

courses.reverse()
print(courses)
courses.sort()
print(courses)
