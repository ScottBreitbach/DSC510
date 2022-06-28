'''how to load JSON files into Python objects
and then write those objects back to JSON files'''
# JSON file with list of state names, abbreviations, and area codes
import json

with open('states.json') as f:      # i think f is just a variable here
    data = json.load(f)

for state in data['states']:
    # print(state)
    # print(state['name'], state['abbreviation'])
    del state['area_codes']

'''dump will dump to JSON file; dumps will dump to JSON string'''
with open('new_states.json', 'w') as f:   # 'w' to give write permission
    json.dump(data, f, indent=2)
