# print(int(4.51))
'''apparently this doesn't work for changing to numbers :('''
from decimal import Decimal
lista = []
listb = []
taco = Decimal(input('gimme number: '))
listb.append(taco)
try:
    taco = Decimal(taco)
    print(taco)
    lista.append(taco)
    print(f'lista is {lista}')
except:
    pass
# listo.append(taco)
# print(listo)
print(f'listb is {listb}')
