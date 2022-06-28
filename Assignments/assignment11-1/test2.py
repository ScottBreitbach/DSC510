var = 'f'
var = float(var)

try:
    var = float(var)
except:
    if var == 'n':
        print("if", var)
    elif var == 'nn':
        print('elif', var)
    else:
        print("else", var)
