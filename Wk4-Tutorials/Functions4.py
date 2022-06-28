
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ['Math', 'Art']   #  pass courses in as positional arguments
info = {'name': 'John', 'age': 22}  # pass info dictionary as keyword arguments

student_info(*courses, **info)
