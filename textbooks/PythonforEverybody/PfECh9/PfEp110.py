
# counts = {'chuck': 1, 'annie': 42, 'jan': 100}
# print(counts.get('jan'))
# print(counts.get('tim', 0))

word = "brontosaurus"
d = {}
for c in word:
    d[c] = d.get(c, 0)+1
print(d)
