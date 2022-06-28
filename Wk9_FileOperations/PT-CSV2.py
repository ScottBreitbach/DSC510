
import csv

# with open('new_names.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter='\t')
#
#     for line in csv_reader:
#         print(line)

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    # for line in csv_reader:
    #     print(line)             # each line is now an ordered dictionary; field names (headers) are now the keys
# Makes it more obvious what you're printing:
#     for line in csv_reader:
#         print(line['email'])

    with open('new_names.csv', 'w') as new_file:
        # fieldnames = ['first_name', 'last_name', 'email']
        fieldnames = ['first_name', 'last_name']


        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')    # ~13:30

        csv_writer.writeheader()    # will write headers out as the first line

        for line in csv_reader:
            del line['email']       # to write only first/last names (see also fieldnames variable above)
            csv_writer.writerow(line)
            # could also have created a new dictionary with only the first and last name keys (omitting email)
            # and pass that into the writerow method

