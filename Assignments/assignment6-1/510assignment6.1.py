# course: DSC510
# assignment: 6.1
# date: 14-Apr-2020
# name: Scott Breitbach
# description: program which prompts the user for a set of temperatures
# and then prints the output from various functions

temperatures = []
while True:
    getTemp = input('Enter a temperature; enter nothing to end: ')
    if getTemp == '' or getTemp == 'nothing': break
    else:           # only adds numbers to the list
        try:
            getTemp = int(getTemp)
        except:
            try:
                getTemp = float(getTemp)
            except:
                continue
        temperatures.append((getTemp))

if not temperatures:
    print('\nNo temperatures were entered. See you next time!')
elif len(temperatures) == 1:
    print(f'\nThe temperature you entered is {temperatures[0]}.\n'
          f'It is both the highest and lowest temperature provided.')
else:
    print(f'\nOf the {len(temperatures)} temperatures provided,\n'
      f'{max(temperatures)} was the highest temperature and\n'
      f'{min(temperatures)} was the lowest temperature.')
