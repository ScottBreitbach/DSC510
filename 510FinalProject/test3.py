'''maybe use this for wind direction'''

# number = float(input("enter number: "))
#
# if number <= 1:
#     print("less than 1")
#     wind_dir = 'N'
# elif number <= 2:
#     print("less than 2")
# elif number <= 3:
#     print("less than 3")
# else:
#     print("more than 3")
'''
N <= 22.5
NE <= 67.5
E <= 112.5
SE <= 157.5
S <= 202.5
SW <= 247.5
W <= 292.5
NW <= 337.5
else N
'''
wind_dir = float(input("some number: "))
if wind_dir <= 22.5:
    direction = 'N'
elif wind_dir <= 67.5:
    direction = 'NE'
elif wind_dir <= 112.5:
    direction = 'E'
elif wind_dir <= 157.5:
    direction = 'SE'
elif wind_dir <= 202.5:
    direction = 'S'
elif wind_dir <= 247.5:
    direction = 'SW'
elif wind_dir <= 292.5:
    direction = 'W'
elif wind_dir <= 337.5:
    direction = 'NW'
else:
    direction = 'N'

print(direction)
