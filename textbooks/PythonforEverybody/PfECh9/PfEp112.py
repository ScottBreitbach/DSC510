# sort by keys alphabetically

counts = {'chuck': 1, 'annie': 42, 'jan': 100}
lst = list(counts.keys())
print(lst)
lst.sort()
for key in lst:
    print(key, counts[key])

# how to sort by counts...?

