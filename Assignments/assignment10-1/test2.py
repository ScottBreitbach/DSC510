SFW = input('SFW? [Y/N]: ')
SFW = SFW.lower()

if (SFW == 'y') or (SFW == 'yes'):
    SFW = True
else:
    SFW = False

if SFW == True:
    print('run SFW program')
else:
    print('run NSFW program')
