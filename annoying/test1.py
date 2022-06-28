# keepGoing = True
# while keepGoing == True:
#     annoying = input("Is this annoying? [Y/N] >> ")
#     annoying = annoying.lower()
#     if annoying == 'y':
#         print("I knew it!")
#         keepGoing = False

keepGoing = True
while keepGoing == True:
    annoying = input("Is this annoying [Yes/No]: ")
    annoying = annoying.lower()
    if annoying == 'yes':
        print("I knew it!")
        keepGoing = False
