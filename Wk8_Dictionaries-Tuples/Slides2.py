statesDict = {
    'California'    : 38802000,
    'Texas'         : 26956000,
    'Florida'       : 19893000,
    'New York'      : 19746000,
    'Illinois'      : 12880000,
    'Pennsylvania'  : 12787000,
    'Ohio'          : 11594000,
    'Georgia'       : 10097000,
    'North Carolina': 9943964,
    'Michigan'      : 9909000,
    'New Jersey'    : 8938000
}

# Iterate using a 'for' loop
for state in statesDict:
    population = statesDict[state]
    print(state, population)

# Iterate using items()
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for key, value in knights.items():
    print("{}: {}".format(key, value))
