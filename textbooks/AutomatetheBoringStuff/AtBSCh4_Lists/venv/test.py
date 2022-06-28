# userName = input('Name: ')
# userAge = input('Age : ')
# print('Hello ' + userName + ", welcome to my app! I never would have guessed you were " + userAge + "!")

# i = 2
# am = 3
# a = 5
# cat = 7
# list = [i, am, a, cat]
# print(list)

# m = ['You', 'are', 'Mary', 'Queen', 'of', 'Scots?']
# print(m[2], "is the",
#       m[3])

x = input('Type "Yes", "No", or "Quit": ')

if (x.upper() == "QUIT"):
    print('Good job')
    exit(0)
elif (x.upper() == "YES"):
    print('Good job')
elif (x.upper() == "NO"):
    print('Good job')
else:
    print('Try again')
