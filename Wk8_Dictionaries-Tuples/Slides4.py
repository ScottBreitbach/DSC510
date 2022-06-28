'''make a list of dictionaries and iterate through'''

carsList = [{'make': 'Toyota', 'model': 'Prius', 'year': 2006, 'doors': 4, 'mileage': 65000},
            {'make': 'Honda', 'model': 'Civic', 'year': 2010, 'doors': 2, 'mileage': 54321},
            {'make': 'Ford', 'model': 'Fusion', 'year': 2012, 'doors': 4, 'mileage': 24680},
            {'make': 'Chevy', 'model': 'Volt', 'year': 2015, 'doors': 4, 'mileage': 7890}]

for carDict in carsList:
    if (carDict['doors'] == 4) and (carDict['mileage'] < 50000):
        print(carDict['make'], carDict['model'], carDict['year'])
