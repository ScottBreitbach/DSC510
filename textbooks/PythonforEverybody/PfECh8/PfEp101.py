
def deleteHead(t):
    del t[0]

def badDeleteHead(t):
    t = t[1:]

def tail(t):
    return t[1:]

letters = ['a', 'b', 'c']
# deleteHead(letters)
badDeleteHead(letters)
print(letters)
rest = tail(letters)
print(rest)
