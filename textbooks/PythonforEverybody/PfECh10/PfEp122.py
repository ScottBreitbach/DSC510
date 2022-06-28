dict = {'a': 10, 'b': 1, 'c': 22}

'''print pairs in a dictionary'''
for key, val in list(dict.items()):
    # print(val, key)
    print(key, val)

'''sort by value in a dictionary (instead of key)'''
l = list()
for key, val in dict.items():
    l.append((val, key))

print(l)
l.sort()
print(l)
