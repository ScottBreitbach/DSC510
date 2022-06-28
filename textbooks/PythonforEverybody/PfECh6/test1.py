# numlist = [1, 2, 3, 4, 5, 22]
# numlist = ['1', '2', '3', '22']
# ', '.join(numlist)
# print(numlist)
# print(str(numlist.count(2)))


def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1

s = ['7', '8', '9', '88']

numList = listToString(s)
print(numList.count('8'))
