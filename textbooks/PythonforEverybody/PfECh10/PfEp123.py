'''reads the text of romeo and juliet, splits into lines,
removes punctuation, splits into words and counts each word.
prints the ten most frequent words'''

import string
fhand = open('h2g2.txt')
counts = {}
for line in fhand:
    line = line.replace('!', ' ')   # fixes H2G2 formatting
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

# Sort the dictionary by value
lst = []
for key, val in list(counts.items()):
    lst.append((val, key))

lst.sort(reverse=True)

for key, val in lst[:30]:
    print(key, val)
