# a = input('enter a temp: ')
# print(type(a))
# print(a)

# testList = [22, 4.4, 33, 7.7, 66]
# testList = [22, 44, 3.3, 77, 66]
# testList = [2.2, 4.4, 33, 7.7, 6.6]
# testList = ['2.2', '4.4', '33', '7.7', '66']
# print(max(testList))
# print(min(testList))

testList = []
something = input('enter a number ')
try:
    something = int(something)
except:
    something = float(something)
testList += [something]
print(testList)
