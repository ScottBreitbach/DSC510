# search and slice string and convert string to float

str = 'X-DSPAM-Confidence:0.8475'
atpos = str.find(':')
extract = str[atpos+1:]
print(type(extract))
extract = float(extract)
print(type(extract))
print(extract)
