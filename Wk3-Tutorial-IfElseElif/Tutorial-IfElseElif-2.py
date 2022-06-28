# Boolean operations:
# and
# or
# not

user = 'Admin'
logged_in = False

if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Creds')

# second example
if not logged_in:
    print('Please Log In')
else:
    print('Welcome')
