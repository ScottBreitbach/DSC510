# Create a new dictionary called "telephone"
telephone = {'mike': '402-555-1212', 'barb': '314-231-8973', 'andy': '515-563-9087'}

# Add a new element to the dictionary
telephone['kelly'] = '402-330-9870'

# Print the dictionary
print(telephone)

# Access the value of the "mike" key
print(telephone['mike'])

# Assign a new value for an existing key
telephone['mike'] = '402-396-9078'

# Find just the keys or the values
print(telephone.keys())
print(telephone.values())

# See if an item is in a dictionary (key or value)
print('mike' in telephone)
print('mike' in telephone.keys())
print('mike' in telephone.values())

# Checking with "if" statements
if 'dirk' in telephone:
    # proceed to use telephone['dirk']
    print(telephone['dirk'])
else:
    # maybe an error message or some action
    exit()
