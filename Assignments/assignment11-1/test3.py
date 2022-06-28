import locale

# moneys = float(input('input # dollars: >> '))

print(locale.setlocale(locale.LC_ALL, ''))

# print(locale.currency(moneys))
#
# print(locale.currency(moneys, grouping=True))

# print(locale.localeconv())
print(dict(locale.localeconv())['currency_symbol'])
# moneys = dict(locale.localeconv())
# print(moneys['currency_symbol'])
moneys = dict(locale.localeconv())['currency_symbol']
print(moneys)
