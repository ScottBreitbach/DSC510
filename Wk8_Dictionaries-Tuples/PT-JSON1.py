'''JSON: JavaScript Object Notation'''
# A common data format for storing some information
'''load a JSON string into a Python object'''
import json

peopleString = '''
{
  "people": [
    {
      "name": "John Smith",
      "phone": "615-555-7164",
      "emails": ["johnsmith@bogusemail.com", "john.smith@work-place.com"],
      "hasLicense": false
    },
    {
      "name": "Jane Doe",
      "phone": "560-555-5143",
      "emails": null,
      "hasLicense": true
    }
  ]
}
'''

data = json.loads(peopleString)
print(data)
print(type(data))       # JSON object gets converted to Python dictionary
print(type(data['people']))     # list

for person in data['people']:
    # print(person)       # prints each person's dictionary
    print(person['name'])   # prints each person's name

