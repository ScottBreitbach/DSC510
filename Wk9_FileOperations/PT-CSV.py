'''called CSV files, even if they're tab, dashes,or other separated instead of comma'''

import csv
#
# with open('names.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)
#
#     print(csv_reader)
#
#     next(csv_reader)    # something around 04:30 in vid
#
#     for line in csv_reader:
#         # print(line)     # prints each line as a list
#         print(line[2])  # print just emails

# open new file and write with - delimiter instead of comma
with open('names.csv', 'r') as csv_file:        # opening file to be read
    csv_reader = csv.reader(csv_file)           # creating csv variable & using .reader to read original file

    with open('new_names.csv', 'w') as new_file:    # open a new file for writing
        # csv_writer = csv.writer(new_file, delimiter='-')    # set variable and open a writer w/delimiter
        csv_writer = csv.writer(new_file, delimiter='\t')   # \t for tab delimiter


        for line in csv_reader:                 # writing each line to new file
            csv_writer.writerow(line)
    # note: it knew to put quotes around the email that contained a dash and hyphenated last name

