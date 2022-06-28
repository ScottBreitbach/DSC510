# passing arguments to a function

def hello_func(greeting, name = 'You'):
    return '{}, {} Function.'.format(greeting, name)

print(hello_func('Hi', name = 'Corey'))

def student_info(*args, **kwargs):  # kw: key word  # * and ** will unpack ...dictionary?
    print(args)     # prints a tuple with all of our positional arguments
    print(kwargs)   # prints a dictionary with all of our keyword values

student_info('Math', 'Art', name='John', age=22)
