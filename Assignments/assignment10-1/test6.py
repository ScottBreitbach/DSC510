'''check if affirmative response is in list'''

affirmative = ['y', 'yes', 'yea', 'yeah', 'yup', 'yuppers', 'please', 'affirmative', 'of course']

def loop():
    var = input('do you want? [Y/N]: ')
    var = var.lower()
    if var in affirmative:
        print('Yes!')
        loop()
    else:
        print('No')
        exit()

loop()
