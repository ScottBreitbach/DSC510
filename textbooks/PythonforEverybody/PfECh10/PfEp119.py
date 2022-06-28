
txt = 'but soft what light through yonder window breaks'
words = txt.split()
# print(words)
t = list()
# print(type(t))
for word in words:
    # print(word)
    t.append((len(word), word))
    # print(t)
# print(t)
t.sort(reverse=True)
# print(t)
res = list()
for length, word in t:
    res.append(word)

print(res)
