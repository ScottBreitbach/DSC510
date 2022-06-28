'''sort by key in a dictionary'''

d = {'a':10, 'b':1, 'c':22}
t = list(d.items())
print(t)
t.sort(reverse=True)
print(t)
