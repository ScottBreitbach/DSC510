'''dump a Python object into a JSON string'''
# remove the phone number and convert back to JSON
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

for person in data['people']:
    del person['phone']

print(data)

newString = json.dumps(data, indent=2)  # indent=2 is # of indentions per item in string (readability)
print(newString)

'''can also sort the keys when passing back to JSON'''

newString = json.dumps(data, indent=2, sort_keys=True)  # now keys are sorted alphabetically

