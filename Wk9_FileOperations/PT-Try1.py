
# f = open('test_File.txt')   # throws an error because file doesn't exist

try:
    f = open('test_File.txt')
    # var = bad_var
# except Exception:           # super vague; will catch all errors
# except FileNotFoundError:
#     print('Sorry. This file does not exist.')
# except Exception:
#     print('Sorry. Something went wrong')    # put the specific exceptions first and general at the bottom
#                                             # because they go in order
except Exception as e:                      # this will print just what the error was
    print(e)                                # in this case: "name 'bad_var' is not defined"
# Can also do that here:
except FileNotFoundError as e:
    print(e)                                # prints: [Errno 2] No such file or directory: 'test_File.txt'

else:
    pass
finally:
    pass
