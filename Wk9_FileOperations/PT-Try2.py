
try:
    f = open('testFile.txt')
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(f.read())     # put these down here; it's better to just put the thing you're trying in try
    f.close()           # or just put it after the try block altogether
finally:
    print("Executing Finally...")


try:
    f = open('curruptFile.txt')
    # if f.name == 'curruptFile.txt':
    #     raise Exception
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print('Error!')
else:
    print(f.read())
    f.close()

