# Program that reads the words in a text file and stores them as keys
# in a dictionary,then counts word instances and prints a list of
# the words and their count.

fname = input('Enter the file name: ')
handle = open(fname)
counts = {}

for line in handle:
    # print('line:', line)
    words = line.split()
    # print('words:', words)
    for word in words:
        counts[word] = counts.get(word, 0) +1

for i in counts:
    print(i, counts[i])

# print('the' in counts)
# print(counts)
