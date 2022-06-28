# Program requests user to input numbers, adds the numbers to a list,
# and performs some maths on them.

numList = []
number = 0

print("Type 'done' when finished.")
while True:
    number = input('Enter a number: ')
    if number == 'done':
        break
    try:
        number = int(number)
        # numList = numList + [number]
    except:
        try:
            number = float(number)
            # numList = numList + [number]
        except:
            print('Invalid input.')
    numList = numList + [number]

print(numList)
print('Total:\t', sum(numList))
print('Count:\t', len(numList))
print('Mean:\t', round((sum(numList)/len(numList)), 2))
print('Max:\t', max(numList))
print('Min:\t',  min(numList))
